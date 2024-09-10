# Changelog

All notable changes to this project will be documented in this file.

## [0.5.4] - 2024-09-10
### Packaging
- Check consistency between tag version and `pyproject.toml` version.
- Added extraction of changelog content for release notes from `CHANGELOG.md`.
- Switched to `actions/attest-build-provenance@v1` from `gh-action-sigstore-python`.

## [0.5.3] - 2024-09-06
### Packaging
- Updated `gh-action-sigstore-python` version to `v3.0.0` in GitHub Actions workflow.

## [0.5.2] - 2024-09-05
### Packaging
- Migrated to `pyproject.toml` and Hatchling build system.
- Added Python 3.12 and 3.13.0-rc.1 to the test matrix.
- Updated CI workflows and actions to the latest versions.
- Enabled attestations for publishing.
- Added publishing to Test PyPI and GitHub releases.
- Dropped support for Python 3.6 and 3.7 due to end-of-life.

## [0.5.1] - 2023-04-27
### Added
- Reverted to original pre-2018 banner format in the IPython shell.
- Minor fixes for banner formatting.

## [0.5.0] - 2023-04-27
### Added
- Implemented a new release format and workflow.
- Drop Python 2.x support.
- Updated dependencies in `setup.py`.

## [0.4.1] - 2022-05-06
### Added
- Universal wheel support added in `setup.cfg`.
- Packaging improvements.

## [0.4.0] - 2019-12-06
### Fixed
- Improved consistency with built-in Flask shell banner format.
- Replaced deprecated `_app_ctx_stack` with `current_app`.

## [0.3.1] - 2018-08-31
### Fixed
- Grammar corrections in docstrings.
- Fixed minor issues with Python 3 compatibility.

## [0.3.0] - 2017-07-25
### Changed
- Migrated to `start_ipython()` for a fully functional shell instead of using an embedded IPython instance.
- Added support for passing CLI arguments to IPython.

## [0.2.2] - 2016-12-06
### Changed
- Updated IPython version to `>=5.0.0` in dependencies.
- Improved banner format to include IPython version.

## [0.2.1] - 2016-07-08
### Removed
- Reverted support for `PYTHONSTARTUP` script handling.

## [0.2.0] - 2016-07-08
### Added
- Added support for IPython `>=5.0.0`.
- Introduced a more consistent banner format for the shell.

## [0.1.1] - 2016-06-20
### Fixed
- Improved the help command text.
- Added proper package metadata in `setup.py`.

## [0.1.0] - 2016-06-20
### Added
- Initial release of `flask-shell-ipython`.
- Replaces the default Flask shell command with IPython.

