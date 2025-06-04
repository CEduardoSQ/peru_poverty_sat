# Contributing

We appreciate your interest in contributing to our work. This document outlines the guidelines and best practices for contributing to ensure a smooth, collaborative, and effective research environment.

## Getting Started

This project follows the [Cookiecutter Data Science][1] directory structure. Understanding this layout is crucial for navigating the repository and knowing where to place your contributions. 

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

Refer to the project's [`README.md`][2] for the detailed setup instructions.

## Contribution Workflow

### [Conventional Commits][3]

We follow the [Conventional Commits][3] specification for commit messages. This helps us maintain a clean commit history and understand the purpose of each change.

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

The scope provides contextual information about the commit's change. It consists of a noun describing a section of the codebase that the commit modifies.

### [GitHub Flow][4]

We follow the [GitHub Flow][4] branching strategy, ensuring a clear and reviewable process for all contributions.


1.  Create a branch from `main` for your contribution. For example:

    - `feat/add-new-model`

    - `fix/bug-in-script`

2.  Make your changes.

3.  Commit your changes, follow the [Conventional Commits][3] specification. For example:
    
    - `feat: add data preprocessing step`

    - `fix: correct typo in README`

4.  Push your branch to the remote repository.

5.  Open a Pull Request from your branch to the `main` branch for review.

### Issues 

We use Issues to track bug and new ideas. When opening an issue, please use the provided templates to help us understand and address your concern efficiently.

1. Go to the [Issues tab][5].
2. Click "New issue" and select the most appropriate template.
3. Fill out the template completely, providing all requested details to clearly describe the bug or proposed feature.

## Contact

If you have any questions, need further clarification, or wish to discuss a contribution before starting work, please reach out to the project maintainer via [eduardo.castro.quispe@gmail.com][6].

<!-- References -->

[1]: https://cookiecutter-data-science.drivendata.org
[2]: README.md
[3]: https://www.conventionalcommits.org
[4]: https://docs.github.com/get-started/using-github/github-flow
[5]: https://github.com/ceduardosq/peru_poverty_sat/issues
[6]: mailto:eduardo.castro.quispe@gmail.com