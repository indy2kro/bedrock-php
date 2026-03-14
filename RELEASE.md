# Release Process

This document describes how to create and publish a new version of Bedrock PHP.

---

## Overview

Bedrock PHP uses a tag-based release model:

- `main` branch: Development version (deployed to `/dev/`)
- Tags (e.g., `v1.0`): Releases (deployed to `/v1.0/`)
- GitHub Action automatically: builds docs, creates zip, deploys to Pages, creates Release

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

### 2. Create and Push Tag

```bash
git tag v1.0
git push origin v1.0 --tags
```

The GitHub Action will automatically:
- Build the documentation to HTML
- Deploy to `/v1.0/`
- Create a zip archive (`bedrock-php-v1.0.zip`)
- Create a GitHub Release with the zip attached

### 3. Update Documentation (Optional)

After the release, you may want to update any external documentation or links that reference the old version.

---

## Directory Structure

The release process creates this structure on the `gh-pages` branch:

```
bedrock-php/
├── index.html          # Version picker (auto-generated)
├── dev/                # Development version
│   └── ...
└── v1.0/               # Released version
    ├── index.html
    ├── src/
    └── bedrock-php-v1.0.zip
```

---

## Rollback

If a release needs to be reverted:

1. Delete the tag: `git push origin :refs/tags/v1.0`
2. Delete the release on GitHub
3. Create a new version tag with fixes (e.g., v1.1 - never reuse version numbers)

---

## Local Testing

To test the build locally before releasing:

```bash
# Install dependencies
pip install mkdocs-material

# Setup
mkdir -p docs/src && cp -r src/* docs/src/
find docs/src -name "*.md" -exec sed -i 's/VERSION_PLACEHOLDER/v1.0/g' {} \;

# Build
python scripts/generate-index.py
mkdocs build -d site/v1.0

# Serve locally
cd site/v1.0
python -m http.server 8080
```

Then open http://localhost:8080 to preview.
