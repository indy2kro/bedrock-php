# Release Process

This document describes how to create and publish a new version of Bedrock PHP.

---

## Overview

Bedrock PHP uses a branch-based release model:

- `main` branch: Development version (deployed to `/dev/`)
- Release branches (e.g., `v1.0`): Frozen releases (deployed to `/v1.0/`)
- Tags: Mark each release version

---

## Prerequisites

1. GitHub repository with GitHub Pages enabled
2. GitHub Actions enabled
3. Push access to the repository

---

## Release Steps

### 1. Prepare the Release

Ensure all content is ready on `main`:

```bash
git checkout main
git pull origin main
```

### 2. Create the Release Branch

Create a new branch for the release:

```bash
git checkout -b v1.0
```

### 3. Add Build Files

Copy the following files from `main` to the release branch:

- `mkdocs.yml` - MkDocs configuration
- `docs/index.md` - Version landing page

Edit `docs/index.md` to update:
- Version number in the title
- Download zip filename

### 4. Commit and Push

```bash
git add mkdocs.yml docs/
git commit -m "Prepare v1.0 release"
git push origin v1.0
```

### 5. Create and Push Tag

```bash
git tag v1.0
git push origin v1.0 --tags
```

The GitHub Action will:
- Build the documentation to HTML
- Deploy to `/v1.0/`
- Create a zip archive

### 6. Create GitHub Release

1. Go to: https://github.com/anomalyco/bedrock-php/releases/new
2. Select the `v1.0` tag
3. Add a title: "Bedrock PHP v1.0"
4. Add description (changelog, highlights)
5. The zip file should be auto-attached from the build
6. Click "Publish release"

### 7. Update Version Picker

Update `docs/root-index.md` in `main` to include the new version:

```markdown
| Version | Description | Status |
|---------|-------------|--------|
| **[v1.0](./v1.0/)** | Stable release | Current |
| **[v1.1](./v1.1/)** | Latest release | Current |
| **[Dev (main)](./dev/)** | Development version | WIP |
```

Commit and push:

```bash
git checkout main
git merge v1.0
git push origin main
```

---

## Directory Structure

After a release, your repository should look like:

```
bedrock-php/
├── main                 # Development
│   ├── mkdocs.yml
│   ├── docs/
│   │   └── root-index.md
│   └── src/
├── v1.0 (branch)        # Released version
│   ├── mkdocs.yml
│   ├── docs/
│   │   └── index.md
│   └── src/
```

---

## Troubleshooting

### GitHub Pages Not Updating

1. Check the Actions tab for build status
2. Verify GitHub Pages source is set to "GitHub Actions"
3. Check the `gh-pages` branch exists

### Zip Not Attached to Release

Manually upload the zip from the Actions artifacts or build locally:

```bash
cd site/v1.0
zip -r bedrock-php-v1.0.zip .
```

### Build Fails

Check `mkdocs.yml` for:
- Valid YAML syntax
- Correct file paths in `nav:` section
- All referenced files exist

---

## Rollback

If a release needs to be reverted:

1. Delete the tag: `git push origin :refs/tags/v1.0`
2. Delete the release on GitHub
3. Create a new version branch with fixes
4. Tag and release as v1.1 (never reuse version numbers)
