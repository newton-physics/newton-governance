#!/usr/bin/env python3
"""Sync CONTRIBUTORS.md from GitHub governance teams.

The source of truth is the GitHub teams that define Newton project roles.
"""

from __future__ import annotations

import argparse
import difflib
import json
import subprocess
import sys
from pathlib import Path


ORG = "newton-physics"
MAINTAINERS_TEAM = "maintainers"
TSC_TEAM = "newton-tsc"
CONTRIBUTORS_PATH = Path("CONTRIBUTORS.md")

TSC_SUFFIXES = {
    "momo-van": " - co-chair",
    "vastsoun": " - co-chair",
}

TEAM_MEMBERS_QUERY = """
query TeamMembers($org: String!, $team: String!, $after: String) {
  organization(login: $org) {
    team(slug: $team) {
      members(first: 100, after: $after, membership: ALL) {
        nodes {
          login
          name
        }
        pageInfo {
          hasNextPage
          endCursor
        }
      }
    }
  }
}
"""


def run_graphql(query: str, **variables: str | None) -> dict:
    cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
    for name, value in variables.items():
        if value is not None:
            cmd.extend(["-F", f"{name}={value}"])

    try:
        completed = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        raise SystemExit("error: GitHub CLI `gh` is required") from None
    except subprocess.CalledProcessError as exc:
        message = exc.stderr.strip() or exc.stdout.strip()
        raise SystemExit(f"error: GitHub API request failed: {message}") from exc

    return json.loads(completed.stdout)


def fetch_team_members(team: str) -> list[dict]:
    users: list[dict] = []
    after: str | None = None

    while True:
        data = run_graphql(TEAM_MEMBERS_QUERY, org=ORG, team=team, after=after)
        team_data = data["data"]["organization"]["team"]
        if team_data is None:
            raise SystemExit(f"error: team `{team}` not found in `{ORG}`")

        connection = team_data["members"]
        users.extend(connection["nodes"])

        page_info = connection["pageInfo"]
        if not page_info["hasNextPage"]:
            return users
        after = page_info["endCursor"]


def display_name(user: dict) -> str:
    login = user["login"]
    name = (user.get("name") or "").strip()
    if name:
        return f"{name} (@{login})"
    return f"@{login}"


def render_entries(users: list[dict], suffixes: dict[str, str] | None = None) -> list[str]:
    suffixes = suffixes or {}
    return [f"* {display_name(user)}{suffixes.get(user['login'], '')}" for user in users]


def render_contributors() -> str:
    maintainers = fetch_team_members(MAINTAINERS_TEAM)
    tsc_members = fetch_team_members(TSC_TEAM)

    lines = [
        "# Community Members",
        "",
        "Please refer to the [contributors data](https://github.com/newton-physics/newton/graphs/contributors) in the repository insights.",
        "",
        "# Maintainers",
        "",
        *render_entries(maintainers),
        "",
        "# TSC Members",
        "",
        *render_entries(tsc_members, TSC_SUFFIXES),
        "",
    ]

    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="exit non-zero if CONTRIBUTORS.md is out of date")
    mode.add_argument("--write", action="store_true", help="update CONTRIBUTORS.md in place")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    rendered = render_contributors()

    if args.write:
        CONTRIBUTORS_PATH.write_text(rendered, encoding="utf-8")
        return 0

    if args.check:
        current = CONTRIBUTORS_PATH.read_text(encoding="utf-8")
        if current == rendered:
            return 0

        diff = difflib.unified_diff(
            current.splitlines(keepends=True),
            rendered.splitlines(keepends=True),
            fromfile=str(CONTRIBUTORS_PATH),
            tofile=f"{CONTRIBUTORS_PATH} (generated)",
        )
        sys.stderr.writelines(diff)
        return 1

    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
