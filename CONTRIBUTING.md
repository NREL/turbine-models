# Contributor's Guide

## Getting started

These contributing guidelines should be read by anyone wishing to contribute code, 
turbines, or documentation changes into the NREL turbine-models library.

1. Create a fork of turbine-models on GitHub
2. Clone your fork of the repository

    ```bash
    git clone https://github.com/<your-GitHub-username>/turbine-models.git
    ```

3. Move into the turbine-models source code directory

    ```bash
    cd turbine-models/
    ```

4. Install turbine-models in editable mode (`-e` flag) to see the changes that are made

    ```bash
    pip install -e ".[dev,docs]"
    ```

## Keeping your fork in sync with NREL/turbine-models

The "main" turbine-models repository is regularly updated with ongoing research at NREL
and beyond. After creating and cloning your fork from the previous section, you will
want to keep it up to date with the latest improvements.

Please note that the below process may introduce merge conflicts with your work, and this does not
provide guidance about how to deal with those conflicts. Here is a good resource for working on
[merge conflicts](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts) that will
inevitably arise in development work.

1. Ensure you're in the turbine-models folder. This may look different depending on your operating system.

   ```bash
   cd /your/path/to/turbine-models/
   ```

2. If you haven't already, add NREL/turbine-models as the "upstream" location (or whichever naming
   convention you prefer).

   ```bash
   git remote add upstream https://github.com/NREL/turbine-models.git
   ```

   To find the name you've given NREL/turbine-models again, you can simply run the following to display
   all the remote sources you're tracking.

   ```bash
   git remote -v
   ```

3. Fetch all the remote changes

   ```bash
   git fetch --all
   ```

4. Sync the upstream (NREL) changes

   ```bash
   git checkout main
   git pull upstream main
   ```

5. Bring your feature branch up to date with the latest changes, assuming you started from the
   main branch.

   ```bash
   git checkout feature/your_contribution
   git merge main
   ```

## Publishing a new release

This project utilizes the [semantic versioning protocol](https://semver.org/). In short,
this means we use a MAJOR.MINOR.PATCH where major versions introduce API-breaking
changes, minor versions introduce new functionality that is backwards compatible, and
patch versions introduce backwards compatible bug fixes.

After a pull request is completed to add new turbines, expand the functionality, or fix
bugs, and the contribution is merged into the main branch, we are ready to create a new
release. The following steps will outline this process, including if anything goes
wrong.

1. Bump the version by the appropriate major, minor, or patch version in
   [`turbine_models/__init__.py`](https://github.com/NREL/turbine-models/blob/main/turbine_models/__init__.py).
2. Date-stamp the unreleased version in
   [`RELEASE.md`](https://github.com/NREL/turbine-models/blob/main/RELEASE.md), and
   ensure the version matches the version used in step 1.
3. Stage, commit, and push the changes.
4. Tag the new version: `git tag -a v1.2.3 -m "Tag message for v1.2.3"`.
5. Push the tag: `git push origin v1.2.3`.
6. Step 5 will trigger the `.github/workflows/publish_to_test_pypi.yml` GitHub Action that
   builds the package and pushes it to Test PyPI. If this is successful, you can move to
   the next step. If unsuccessful, follow the below steps.
   1. Delete the tag locally (`git tag -d v1.2.3`) and on the remote
      (`git push --delete origin v1.2.3`)
   2. Address the build or publishing errors in the GitHub Action.
   3. Repeat the process starting back to step 3 in the main instructions.
7. Create a new release with release notes, using the new tag at
   https://github.com/NREL/turbine-models/releases/new. Once published, this will
   trigger the `.github/workflows/publish_to_pypi.yml` GitHub Action that publishes
   the new release on PyPI. If this is unsuccessful, follow the substeps for step 6,
   except that you will be unable to republish to Test PyPI because PyPI and Test PyPI
   releases can only happen exactly once for a version, unlike GitHub.
