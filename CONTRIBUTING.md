# Contributing

We appreciate your interest in the project. This document outlines the guidelines for contributing.

## Getting Started

This project follows the [Cookiecutter Data Science][cookiecutter] directory structure. Understanding this layout is crucial for navigating the repository and knowing where to place your contributions.

```
├── .github/            # GitHub specific configurations.
├── data/               # All data.
│   ├── external/       # External data.
│   ├── interim/        # Intermediate data.
│   ├── processed/      # Processed data.
│   └── raw/            # Raw data.
├── notebooks/          # Jupyter notebooks.
├── .gitignore          # Exclude files and directories from version control.
├── CONTRIBUTING.md     # Provides guidelines for contributing to the project.
├── environment.yml     # Defines the environment dependencies.
├── Makefile            # Automates development tasks.
└── README.md           # Provides an overview of the project.
```

Refer to the [`README.md`](README.md) for the detailed setup instructions.

## Contribution Workflow

### [Conventional Commits][conventional-commits]

We follow the [Conventional Commits][conventional-commits] specification for commit messages. This helps us maintain a clean commit history and understand the purpose of each change.

A commit message should be structured as follows:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

The recommended length for the first line is 50 characters, and the rest should be wrapped at 72 characters.

**`type`:**

- `feat`: Introduces a new feature.

- `fix`: Patches a bug.

- `test`: Changes to the tests.

- `docs`: Changes to the documentation.

- `build`: Changes to the build system or external dependencies.

- `ci`: Changes to the CI configuration files and scripts.

- `perf`: Changes to the performance.

- `refactor`: Changes to the internal structure of the code without altering the effectiveness and efficiency.

**`scope`:**

The scope provides additional contextual information about the commit change. It consists of a noun describing a section of the codebase that the commit modifies.

### [GitHub Flow][github-flow]

We follow the [GitHub Flow][github-flow] branching strategy, ensuring a clear and reviewable process for all contributions.


1.  Create a new branch from `main` for your contribution. For example:

    - `feat/add-new-model`

    - `fix/bug-in-script`

2.  Make your changes.

3.  Commit your changes, follow the [Conventional Commits][conventional-commits] specification. For example:

    - `feat: add data preprocessing step`

    - `fix: correct typo in README`

4.  Push your branch to the remote repository.

5.  Open a Pull Request from your branch to the `main` branch for review.

### Issues

We use Issues to track bugs and new ideas. Before opening a new issue,  check the existing issues to avoid duplicates. Use the provided templates to help us understand and address your concern efficiently.

1. Go to the ["Issues"][issues] tab.
2. Click ["New issue"][new-issue] and select the most appropriate template.
3. Fill out the template, providing all requested details to clearly describe it.

## Contact

If you have any questions, need further clarification, or wish to discuss a contribution before starting work, please reach out to the project maintainer via [eduardo.castro.quispe@gmail.com](mailto:eduardo.castro.quispe@gmail.com).

<!-- References -->

[conventional-commits]: https://www.conventionalcommits.org
[cookiecutter]: https://cookiecutter-data-science.drivendata.org
[github-flow]: https://docs.github.com/get-started/using-github/github-flow
[issues]: https://github.com/ceduardosq/peru_poverty_sat/issues
[new-issue]: https://github.com/CEduardoSQ/peru_poverty_sat/issues/new/choose
