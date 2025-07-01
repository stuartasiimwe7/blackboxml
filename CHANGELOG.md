# Changelog

All notable changes to this project will be documented in this file. This project adheres to [Semantic Versioning](https://semver.org/).

## [0.2.0] - 2025-07-02
### Major Release: traceML Rebranding and Feature Enhancements

#### Added
- **Rebranding:** The package has been fully rebranded from `blackboxml` to `traceML` (user-facing) and `traceml` (module/package). All code, documentation, and metadata now reflect the new name, providing a unified and professional identity.
- **Log Directory Update:** All training and experiment logs are now saved in the `traceml_logs/` directory instead of the previous `blackbox_logs/`. This change ensures consistency with the new package name and avoids confusion for new users.
- **Plot Saving Capability:** The `visualise_metrics` function now supports saving plots as image files. Users can specify a directory to save plots, making it easier to archive and share training results.
- **Comprehensive Documentation:** Updated and expanded documentation, including a new API reference and migration instructions for users upgrading from `blackboxml`.
- **Changelog:** Introduced this `CHANGELOG.md` to provide transparent and detailed tracking of all changes, improvements, and fixes.

#### Changed
- **Import Paths and Usage Examples:** All import statements, usage examples, and references in the codebase and documentation now use `traceML`/`traceml` instead of `blackboxml`.
- **Metadata and URLs:** All project metadata, including PyPI and GitHub URLs, have been updated to reflect the new package name and repository location.
- **Consistent Branding:** All user-facing messages, logs, and documentation now consistently use the `traceML` branding, ensuring a professional and cohesive user experience.

#### Removed
- **Deprecation Warnings:** All deprecation warnings and references to `blackboxml` have been removed from the codebase.
- **Legacy Artifacts:** Old log directories (`blackbox_logs/`) and build artifacts related to `blackboxml` have been deleted to prevent confusion and ensure a clean environment for new users.

---

## [0.1.1] - 2025-07-01
### Final blackboxml Release (Deprecated)

#### Deprecated
- **Deprecation Notice:** This was the final release of `blackboxml`. It included clear deprecation warnings and migration instructions, guiding users to upgrade to the new `traceML` package for continued support and new features. 