# Changelog

All notable changes to this project will be documented in this file. This project adheres to [Semantic Versioning](https://semver.org/).

## [0.2.0] - 2025-07-02
### Feature and Maintenance Update

#### Added
- **Type Hints and Improved Docstrings:** All public functions and classes now include type hints and comprehensive docstrings for better maintainability and editor support.
- **Switch to Python Logging Module:** All print statements have been replaced with the Python `logging` module, providing users with more control over log output and integration with other tools.
- **Error Handling in Visualiser:** The visualiser now includes robust error handling to gracefully manage missing or malformed log files, providing clear and actionable feedback to users.

#### Changed
- **Consistent Naming:** All user-facing messages, import paths, and documentation now consistently use the `BlackBoxML`/`blackboxml` branding.

---

## [0.1.0] - April 2025 Initial Release
- First public release of BlackBoxML, providing automatic metric logging for Keras/TensorFlow workflows.

#### Added

- **Plot Saving Capability:** The `visualise_metrics` function now supports saving plots as image files. Users can specify a directory to save plots, making it easier to archive and share training results.
- **Comprehensive Documentation:** Updated and expanded documentation, including a new API reference and migration instructions for users upgrading from `blackboxml`.
- **Changelog:** Introduced this `CHANGELOG.md` to provide transparent and detailed tracking of all changes, improvements, and fixes.

