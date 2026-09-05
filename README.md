# Newton Governance

This repository hosts documents related to Newton project governance and legal, and guidelines that apply to the repositories in the `newton-physics` organization.

Newton is a [Linux Foundation](https://www.linuxfoundation.org/) project that is community-built and maintained. It is permissively licensed under the Apache-2.0 license.

The project was initiated by [Disney Research](https://www.disneyresearch.com/), [Google DeepMind](https://deepmind.google/), and [NVIDIA](https://www.nvidia.com/).

## Contributor List

Sync the Maintainers and TSC sections in [CONTRIBUTORS.md](CONTRIBUTORS.md) from the `newton-physics` GitHub organization governance teams:

Prerequisites:

* Python 3.
* GitHub CLI `gh`.
* An authenticated `gh` session with access to read the `newton-physics` organization teams. Check with `gh auth status`.

Run the script from this repository root:

```bash
python3 scripts/sync_contributors.py --write
python3 scripts/sync_contributors.py --check
```

The `--write` command updates `CONTRIBUTORS.md` in place. The `--check` command exits non-zero and prints a diff when `CONTRIBUTORS.md` is out of date.
