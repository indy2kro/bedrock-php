#!/usr/bin/env python3
"""
Generate version index for Bedrock PHP documentation.

Scans existing version directories and generates an index page
with a table of all available versions.
"""

import os
import re
from pathlib import Path


def discover_versions(sitegh_pages_path: str) -> list[tuple[str, str, str]]:
    """
    Discover existing versions from gh-pages directory.
    
    Returns list of tuples: (version_dir, version_display, status)
    """
    versions = []
    base_path = Path(sitegh_pages_path)
    
    if not base_path.exists():
        return versions
    
    # Scan for version directories
    for item in base_path.iterdir():
        if item.is_dir():
            dir_name = item.name
            
            # Match v1.0, v1.1, etc.
            if re.match(r'^v\d+\.\d+', dir_name):
                versions.append((dir_name, dir_name, "stable"))
            
            # Match dev
            elif dir_name == "dev":
                versions.append((dir_name, "Dev (main)", "development"))
    
    # Sort versions: dev first, then by version number (newest first)
    def sort_key(v):
        if v[0] == "dev":
            return ("", "")  # dev first
        # Extract version number for sorting
        match = re.search(r'v(\d+)\.(\d+)', v[0])
        if match:
            return (match.group(1), match.group(2))
        return v
    
    versions.sort(key=sort_key, reverse=True)
    
    return versions


def generate_index(versions: list[tuple[str, str, str]], current_version: str) -> str:
    """Generate the index.md content."""
    
    # Determine status for current version
    def get_status_display(version_dir: str, status: str) -> str:
        if version_dir == current_version:
            return "Current"
        elif status == "development":
            return "WIP"
        else:
            return "Previous"
    
    # Build table rows
    rows = []
    for version_dir, version_display, status in versions:
        status_display = get_status_display(version_dir, status)
        link = f"[{version_display}](./{version_dir}/)"
        
        # Find zip file
        zip_name = f"bedrock-php-{version_dir}.zip"
        
        rows.append(f"| {link} | [Download](./{version_dir}/{zip_name}) | {status_display} |")
    
    table_rows = "\n".join(rows)
    
    # Build full index content
    index_content = f"""# Bedrock PHP — Select a Version

## Available Versions

Choose a version to view:

| Version | Download | Status |
|---------|----------|--------|
{table_rows}

---

## What is Bedrock PHP?

Bedrock PHP is an **operational standard** for building, deploying, and running PHP applications in production.

It is intentionally restrictive. Its goal is to define a **safe, boring, repeatable baseline** that:

- reduces decision fatigue
- minimizes accidental complexity
- survives team and context changes
- remains understandable months or years later

If Bedrock PHP feels limiting, that is by design.

---

## Links

- [View on GitHub](https://github.com/anomalyco/bedrock-php)
"""
    
    return index_content


def main():
    """Main entry point."""
    # Determine current version from git ref or environment
    current_version = os.environ.get("VERSION_DIR", "dev")
    
    # Path to existing gh-pages content (passed as argument)
    sitegh_pages_path = os.environ.get("SITE_GH_PAGES_PATH", "sitegh-pages")
    
    # Discover versions
    versions = discover_versions(sitegh_pages_path)
    
    # Always ensure dev is included if we're building dev
    if current_version == "dev":
        has_dev = any(v[0] == "dev" for v in versions)
        if not has_dev:
            versions.insert(0, ("dev", "Dev (main)", "development"))
    
    # Generate index
    index_content = generate_index(versions, current_version)
    
    # Write to docs/index.md (in current directory for mkdocs to pick up)
    output_path = Path("docs") / "index.md"
    output_path.write_text(index_content, encoding="utf-8")
    
    print(f"Generated index with {len(versions)} versions: {[v[0] for v in versions]}")


if __name__ == "__main__":
    main()
