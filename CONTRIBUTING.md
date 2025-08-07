The content of this file is adapted from [the OpenVBD project contribution guidelines](https://github.com/AcademySoftwareFoundation/openvdb/blob/master/CONTRIBUTING.md).

# Overview

Newton is a project of the Linux Foundation and aims to be governed in a transparent, accessible way for the benefit of the community. All participation in this project is open and not bound to corporate affiliation. Participants are all bound to the Linux Foundation [Code of Conduct](https://lfprojects.org/policies/code-of-conduct/).

# Contributing to Newton

Newton welcomes contributions from the community. To avoid any surprises and increase the chance of contributions being merged, we encourage contributors to communicate their plans proactively by opening a GitHub Issue or starting a Discussion. Ways to contribute include:

## Questions, Discussions, Suggestions

* Help answer questions or contribute to technical discussion in [GitHub Discussions](https://github.com/newton-physics/newton/discussions) and Issues.
* If you have a question, suggestion or discussion topic, start a new [GitHub Discussion](https://github.com/newton-physics/newton/discussions) if there is no existing topic.
* Once somebody shares a satisfying answer to the question, click "Mark as answer".
* [GitHub Issues](https://github.com/newton-physics/newton/issues) should only be used for bugs and features. Specifically, issues that result in a code or documentation change. We may convert issues to discussions if these conditions are not met.

## Reporting a Bug

* Check in the [GitHub Issues](https://github.com/newton-physics/newton/issues) if a report for the bug already exists.
* If the bug has not been reported yet, open a new Issue.
* Use a short, descriptive title and write a clear description of the bug.
* Document the Git hash or release version where the bug is present, and the hardware and environment by including the output of `nvidia-smi`.
* Add executable code samples or test cases with instructions for reproducing the bug.

## Documentation Issues

* Create a new issue if there is no existing report, or
* directly submit a fix following the "Fixing a Bug" workflow below.

## Fixing a Bug

* Ensure that the bug report issue has no assignee yet. If the issue is assigned and there is no linked PR, you're welcome to ask about the current status by commenting on the issue.
* Write a fix and regression unit test for the bug following the [style guide](https://newton-physics.github.io/newton/development-guide.html#style-guide).
* Open a new pull request for the fix and test.
* Write a description of the bug and the fix.
* Mention related issues in the description: E.g. if the patch fixes Issue \#33, write Fixes \#33.
* Have a signed CLA on file (see [Legal Requirements](#legal-requirements)).
* Have the pull request approved by a [Project Member](#project-members) and merged into the codebase.

## Improving Performance

* Write an optimization that improves an existing or new benchmark following the [style guide](https://newton-physics.github.io/newton/development-guide.html#style-guide).
* Open a new pull request with the optimization, and the benchmark, if applicable.
* Write a description of the performance optimization.
* Mention related issues in the description: E.g. if the optimization addresses Issue \#42, write Addresses \#42.
* Have a signed CLA on file (see [Legal Requirements](#legal-requirements)).
* Have the pull request approved by a [Project Member](#project-members) and merged into the codebase.

## Adding a Feature or Solver

* Discuss your proposal ideally before starting with implementation. Open a GitHub Issue or Discussion to:
  * propose and motivate the new feature or solver;
  * detail technical specifications;
  * and list changes or additions to the Newton API.
* Wait for feedback from [Project Members](#project-members) before proceeding.
* Implement the feature or solver following the [style guide](https://newton-physics.github.io/newton/development-guide.html#style-guide).
* Add comprehensive testing and benchmarking for the new feature or solver.
* Ensure all existing tests pass and that existing benchmarks do not regress.
* Update or add documentation for the new feature or solver.
* Have a signed CLA on file (see [Legal Requirements](#legal-requirements)).
* Have the pull request approved by a [Project Member](#project-members) and merged into the codebase.

## Adding Simulation Assets

* Before proposing to add any assets to the Newton project, make sure that the assets are properly licensed for use and distribution. If you are unsure about the license, open a new discussion.
* The Newton project hosts possibly large simulation assets such as models, textures, datasets, or pre-trained policies in the [newton-assets](https://github.com/newton-physics/newton-assets) repository to keep the main newton repository small.
* Therefore, along with a pull request in the main newton repository that relies on new assets, open a corresponding pull request in the [newton-assets](https://github.com/newton-physics/newton-assets) repository.
* Make sure to include the license information by adding to the [LICENSE](https://github.com/newton-physics/newton-assets/blob/main/LICENSE) file in the [newton-assets](https://github.com/newton-physics/newton-assets) root.
* Have a signed CLA on file (see [Legal Requirements](#legal-requirements)).
* Have the pull request approved by a [Project Member](#project-members) and merged into the asset repository.

# Legal Requirements

Newton follows the open source software best practice policies of the Linux Foundation.

## License

Newton is licensed under the [Apache License, version 2.0](LICENSE.md) license. Contributions to Newton should be compatible with that standard license. Newton documentation will be received and made available under the Creative Commons Attribution 4.0 International License.

## Contributor License Agreements

Developers who wish to contribute code to be considered for inclusion in Newton must first complete a **Contributor License Agreement**.

Newton uses [EasyCLA](https://lfcla.com/) for managing CLAs, which automatically checks to ensure CLAs are signed by a contributor before a commit can be merged.

* If you are an individual writing the code on your own time and you're SURE you are the sole owner of any intellectual property you contribute, you can sign the CLA as [an individual contributor](https://docs.linuxfoundation.org/lfx/easycla/contributors/individual-contributor) (ICLA).

* If you are writing the code as part of your job, or if there is any possibility that your employers might think they own any intellectual property you create, then you should use the [Corporate Contributor](https://docs.linuxfoundation.org/lfx/easycla/contributors/corporate-contributor) License Agreement (CCLA).

The Newton CLAs are the standard forms used by Linux Foundation projects and [recommended by the ASWF TAC](https://tac.aswf.io/process/contributing.html#contributor-license-agreement-cla). The Newton ICLA and CCLA are available in the [legal subfolder](legal).

# Project Roles

The Newton Project defines four project roles:

1. Community Members
2. Project Members
3. Maintainers
4. Technical Steering Committee (TSC) Members

See list in [CONTRIBUTORS.md](CONTRIBUTORS.md) for project members and their roles.

## Community Members

The Community Member role is equivalent to the Contributor role in the [charter](legal/Charter.pdf). It is the starting role for anyone participating in the project in any of the ways described in the [Contributing to Newton](#contributing-to-newton) Section above.

## Project Members

The Project Member role is the equivalent of the "Committer" role in the [charter](legal/Charter.pdf).

This role enables the participant to review and approve pull requests as part of the project-members team of the newton-physics GitHub organization, but also comes with the obligation to be a responsible leader in the community.

### Process for Becoming a Project Member

* Show your experience with the codebase through contributions and engagement on the project communication channels.
* Request to become a Project Member.
* Have the majority of Project Members approve you becoming a Project Member, or be assigned the Project Member role at the discretion of a Maintainer or the TSC.
* Your name is added to the list of Project Members in the [CONTRIBUTORS.md](CONTRIBUTORS.md) file for the project and you are added to the newton-physics GitHub organization project-members team.

### Project Member responsibilities

* Monitor project-related communication channels such as email aliases, GitHub discussions, etc.
* Triage GitHub issues and manage GitHub discussions.
* Perform pull request reviews.
* Make sure that ongoing PRs are moving forward at the right pace or close them.
* Remain an active contributor to the project in general and the code base in particular.

### When Does a Project Member Lose Project Member Status?

If a Project Member is no longer interested or cannot perform the Project Member duties listed above, they should volunteer to be moved to emeritus/emerita status. In extreme cases, this can also occur by a vote of the TSC per [the voting process below](#conflict-resolution-and-voting).

## Maintainers

In addition to the rights and obligations of Project Members, this role grants maintenance access to all repositories in the project.

### Process for Becoming a Maintainer

* Be a Project Member and request to become a Maintainer.
* Have the majority of Maintainers approve you becoming a Maintainer, or be assigned the Maintainer role at the discretion of the TSC.
* Your name is added to the list of Maintainers in the [CONTRIBUTORS.md](CONTRIBUTORS.md) file for the project and you are added to the Maintainers team.

### Maintainer Responsibilities

* All responsibilities of Project Members.
* Manage repository settings like branch protection rules, and manage project-wide settings and teams.
* Oversee health of all project repositories.
* Ensure compliance with project policies and community guidelines.
* Coordinate and execute releases, and make sure release processes are followed and documented.

### When Does a Maintainer Lose Maintainer Status?

The conditions and process are the same as for Project Members, see above.

## Technical Steering Committee (TSC) member

The Technical Steering Committee (TSC) oversees the overall technical direction of Newton, as defined in the [charter](legal/Charter.pdf).

TSC members consist of project members that have been nominated by the TSC, with a supermajority of members required to have a member elected to be a TSC member.

The TSC will elect two co-chairs among its members. The responsibility of the co-chairs is to coordinate TSC duties, and preside over TSC meetings and communicate meeting summaries and decisions to the community.

A voting member of the TSC may nominate a successor in the event that such voting member decides to leave the TSC, and the TSC, including the departing member, shall confirm or reject such nomination by a vote. In the event that the departing member's nomination for successor is rejected by vote of the TSC, the departing member shall be entitled to continue nominating successors until one such successor is confirmed by vote of the TSC. If the departing member fails or is unable to nominate a successor, the TSC may nominate one on the departing member's behalf.

All meetings of the TSC are open to participation by any member of the Newton community. Meeting times are listed in the Newton community calendar.

# Release Process

Project releases will occur on a scheduled basis as agreed to by the TSC.

# Conflict resolution and voting

In general, we prefer that technical issues and role memberships are amicably worked out between the persons involved. If a dispute cannot be decided independently, the TSC can be called in to decide an issue. If the TSC themselves cannot decide an issue, the issue will be resolved by voting. The voting process is a simple majority in which each TSC member receives one vote.

# Communication

This project, just like all of open source, is a global community. In addition to the LF [Code of Conduct](https://lfprojects.org/policies/code-of-conduct/), this project will:

* Keep all communication on open channels (mailing list, forums, chat).
* Be respectful of time and language differences between community members (such as scheduling meetings, email/issue responsiveness, etc).
* Ensure tools are able to be used by community members regardless of their region.

If you have concerns about communication challenges for this project, please contact the TSC.
