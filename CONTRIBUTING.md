# Contributing

We appreciate your interest in contributing to our work. This document outlines the guidelines for contributing to the project.

## Directory Structure

This project follows the [Cookiecutter Data Science][cookiecutter] directory structure. Understanding this layout is crucial for navigating the repository and knowing where to place your contributions.

```
├── .github/            # GitHub specific configurations.
├── CONTRIBUTING.md     # Guidelines for contributing to the project.
├── data/
│   ├── external/       # Data from third party sources.
│   ├── interim/        # Intermediate data that has been transformed.
│   ├── processed/      # The final, canonical data sets for modeling.
│   └── raw/            # The original, immutable data dump.
├── environment.yml     # The environment file.
├── notebooks/          # Jupyter notebooks.
└── README.md           # The top-level README for developers using this project.
```

## Environment

This project uses a [`conda`][conda] environment to manage the dependencies.

1. Export the environment with the `--from-history` flag to ensure cross-platform compatibility:

```sh
conda export --from-history --file environment.yml
```

2. Remove the prefix from the environment file; however, maintain the environment name.

```yml
name: peru_poverty_sat
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10.10
```

## Contribution Workflow

### [Conventional Commits][conventionalcommits]

This project follow the [Conventional Commits][conventionalcommits] specification for commit messages. It helps us maintain a clean commit history and understand the purpose of each change.

A commit message should be structured as follows:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

**Types:**

- `feat`: Introduces a new feature to the codebase.

- `fix`: Patches a bug in the codebase.

- `build`: Changes that affect the build system or external dependencies.

- `ci`: Changes to the CI configuration files and scripts.

- `docs`: Changes to the documentation.

- `perf`: A code change that improves performance.

- `test`: Adding or correcting tests.

- `refactor`: A code change that improves the internal structure of the code without altering the effectiveness and efficiency.

**Scope (optional):**

The scope provides contextual information about the commit change. It consists of a noun describing a section of the codebase that the commit modifies.

### [GitHub Flow][github-flow]

We follow the [GitHub Flow][github-flow] branching strategy, ensuring a clear and reviewable process for all contributions.

1.  Create a branch from `main` for your contribution. For example:

    - `feat/add-new-model`

    - `fix/bug-in-script`

2.  Make your changes.

3.  Commit your changes, follow the [Conventional Commits][conventionalcommits] specification. For example:

    - `feat: add data preprocessing step`

    - `fix: correct typo in README`

4.  Push your branch to the remote repository.

5.  Open a Pull Request from your branch to the `main` branch for review.

### Issues

Use an Issue to track a bug or idea. Make use of the templates to explain the issue.

1. Go to the ["Issues"][issues] tab.
2. Click ["New issue"][choose] and select the most appropriate template.
3. Fill out the template completely, providing all requested details to clearly describe the bug or proposed feature.

## Contact

If you have any questions, need further clarification, or wish to discuss a contribution before starting work, please reach out to the project maintainer via [eduardo.castro.quispe@gmail.com][mail].

<!-- References -->

[choose]: https://github.com/CEduardoSQ/peru_poverty_sat/issues/new/choose
[conda]: https://docs.conda.io
[cookiecutter]: https://cookiecutter-data-science.drivendata.org
[conventionalcommits]: https://www.conventionalcommits.org
[github-flow]: https://docs.github.com/get-started/using-github/github-flow
[issues]: https://github.com/ceduardosq/peru_poverty_sat/issues
[mail]: mailto:eduardo.castro.quispe@gmail.com
