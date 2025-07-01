# Contributing to traceML

Thank you for your interest in contributing to **traceML**! 
We welcome contributions from everyone — whether it's fixing bugs, improving documentation, or adding new features.  
Your efforts help push traceML forward. 

---

## How to Contribute

### 1. Fork and Clone the Repository

- Fork the repository on GitHub.
- Clone your fork to your local machine using one of the following methods:

  - **HTTPS**:
    ```bash
    git clone https://github.com/stuartasiimwe7/traceml.git
    ```

  - **GitHub CLI**:
    ```bash
    gh repo clone stuartasiimwe7/traceml
    ```

  - **SSH**:
    ```bash
    git clone git@github.com:stuartasiimwe7/traceml.git
    ```

- Navigate into the project directory:
  ```bash
  cd traceml
  ```

### 2. Set Up Your Development Environment

- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### 3. Create a Feature Branch

- Create a new branch for your work:
  ```bash
  git checkout -b feature/your-feature-name
  ```
- Use descriptive branch names like `fix/logger-bug` or `feat/add-new-metrics`.

### 4. Make Your Changes

- Fix bugs, add features, or improve documentation.
- Follow the existing coding style (PEP8) and best practices.

### 5. Test Your Changes

- Run tests to validate your work:
  ```bash
  pytest
  ```

### 6. Commit and Push

- Stage and commit your changes:
  ```bash
  git add .
  git commit -m "Fix: Correct metric calculation for accuracy"
  git push origin feature/your-feature-name
  ```

### 7. Submit a Pull Request

- Open a pull request (PR) against the `main` branch.
- Provide a clear description of your changes and link any relevant issues.
- Make sure all automated checks pass before submitting. Please follow the [Pull Request Template](../.github/PULL_REQUEST_TEMPLATE.MD).

### 8. Participate in Code Review

- Respond to feedback constructively and revise if needed.
- Code reviews are here to make the project (and you) even better.

---

## Guidelines

### Code Style

- Follow [PEP8](https://www.python.org/dev/peps/pep-0008/).
- Write modular, readable, and well-documented code.

### Reporting Issues

- Check existing issues first.
- Provide clear reproduction steps.
- Use the [Bug Report Template](../.github/ISSUE_TEMPLATE/bug_report.md).

### Adding New Features

- Open an issue first if proposing major changes.
- Include appropriate tests and documentation.

---

## License

By contributing, you agree your work will be licensed under the same license as **traceML**.

---

Thanks for being awesome,  
**The traceML Team** 🖤