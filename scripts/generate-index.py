#!/usr/bin/env python3
"""
Generate version index for Bedrock PHP documentation.

Scans existing version directories and generates:
1. docs/index.md - for MkDocs navigation
2. site/index.html - standalone version picker for root
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


def generate_index_md(versions: list[tuple[str, str, str]], current_version: str) -> str:
    """Generate the index.md content for MkDocs."""
    
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


def generate_index_html(versions: list[tuple[str, str, str]], current_version: str) -> str:
    """Generate standalone HTML version picker."""
    
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
        zip_name = f"bedrock-php-{version_dir}.zip"
        
        rows.append(f"""        <tr>
            <td><a href="{version_dir}/">{version_display}</a></td>
            <td><a href="{version_dir}/{zip_name}">Download</a></td>
            <td>{status_display}</td>
        </tr>""")
    
    table_rows = "\n".join(rows)
    
    html = f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bedrock PHP - Select a Version</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            margin-bottom: 10px;
        }}
        .subtitle {{
            color: #666;
            margin-bottom: 30px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #eee;
        }}
        th {{
            background: #f9f9f9;
            font-weight: 600;
        }}
        a {{
            color: #0066cc;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .description {{
            color: #666;
            line-height: 1.6;
            margin-top: 30px;
        }}
        .description ul {{
            margin: 10px 0;
        }}
        .links {{
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #eee;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Bedrock PHP</h1>
        <p class="subtitle">Select a Version</p>
        
        <table>
            <thead>
                <tr>
                    <th>Version</th>
                    <th>Download</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
{table_rows}
            </tbody>
        </table>
        
        <div class="description">
            <p>Bedrock PHP is an <strong>operational standard</strong> for building, deploying, and running PHP applications in production.</p>
            <p>It is intentionally restrictive. Its goal is to define a <strong>safe, boring, repeatable baseline</strong> that:</p>
            <ul>
                <li>reduces decision fatigue</li>
                <li>minimizes accidental complexity</li>
                <li>survives team and context changes</li>
                <li>remains understandable months or years later</li>
            </ul>
            <p>If Bedrock PHP feels limiting, that is by design.</p>
        </div>
        
        <div class="links">
            <a href="https://github.com/anomalyco/bedrock-php">View on GitHub</a>
        </div>
    </div>
</body>
</html>"""
    
    return html


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
    
    # Generate both formats
    index_md = generate_index_md(versions, current_version)
    index_html = generate_index_html(versions, current_version)
    
    # Write docs/index.md (for MkDocs navigation)
    output_path = Path("docs") / "index.md"
    output_path.write_text(index_md, encoding="utf-8")
    
    # Write site/index.html (standalone version picker)
    # This will be copied to site/ after MkDocs build
    site_index_path = Path("site") / "index.html"
    site_index_path.parent.mkdir(parents=True, exist_ok=True)
    site_index_path.write_text(index_html, encoding="utf-8")
    
    print(f"Generated index with {len(versions)} versions: {[v[0] for v in versions]}")


if __name__ == "__main__":
    main()
