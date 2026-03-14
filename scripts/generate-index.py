#!/usr/bin/env python3
"""
Generate version index for Bedrock PHP documentation.

Scans existing version directories and generates:
1. docs/index.md - for MkDocs navigation (without version table)
2. site/index.html - standalone version picker for root (with version table)
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


def generate_mkdocs_index(versions: list[tuple[str, str, str]], current_version: str) -> str:
    """Generate the index.md content for MkDocs (without version table)."""
    
    # Build full index content - no version table, just intro
    index_content = f"""# Bedrock PHP — v1.0

## What This Is

Bedrock PHP is an **operational standard** for building, deploying, and running PHP applications in production.

It is intentionally restrictive.

Its goal is not to define the best possible system, but to define a **safe, boring, repeatable baseline** that:

- reduces decision fatigue
- minimizes accidental complexity
- survives team and context changes
- remains understandable months or years later

If Bedrock PHP feels limiting, that is by design.

---

## Contents

- [Chapter 1: Purpose & Scope](src/chapter1_purpose_and_scope.md)
- [Chapter 2: Adoption Model](src/chapter2_adoption_model.md)
- [Chapter 3: Core Values (Operational)](src/chapter3_core_values.md)
- [Chapter 4: Declared Defaults](src/chapter4_declared_defaults.md)
- [Chapter 5: Deployment & Infrastructure](src/chapter5_deployment_infrastructure.md)
- [Chapter 6: Configuration & State](src/chapter6_configuration_state.md)
- [Chapter 7: Observability](src/chapter7_observability.md)
- [Chapter 8: Performance & Scaling Limits](src/chapter8_performance_scaling_limits.md)
- [Chapter 9: Security Posture](src/chapter9_security_posture.md)
- [Chapter 10: Maintenance & Decommissioning](src/chapter10_maintenance_decommissioning.md)
- [Chapter 11: When to Leave Bedrock PHP](src/chapter11_when_to_leave.md)
- [Chapter 12: Version Policy](src/chapter12_version_policy.md)

---

## Downloads

- [bedrock-php-{current_version}.zip](./bedrock-php-{current_version}.zip) — Source markdown files
"""
    
    return index_content


def generate_index_html(versions: list[tuple[str, str, str]], current_version: str) -> str:
    """Generate standalone HTML version picker with dark theme."""
    
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
<html lang="en" class="no-js">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bedrock PHP - Select a Version</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">
    <style>
        :root {{
            --pico-background-color: #242937;
            --pico-card-background-color: #2a2f3e;
            --pico-card-border-color: #3a4055;
            --pico-color: #e4e4e7;
            --pico-muted-color: #a1a1aa;
            --pico-primary: #6366f1;
            --pico-primary-hover: #818cf8;
        }}
        body {{
            background-color: #1a1d29;
            color: #e4e4e7;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 700px;
            width: 100%;
        }}
        h1 {{
            color: #e4e4e7;
            margin-bottom: 5px;
            text-align: center;
        }}
        .subtitle {{
            color: #a1a1aa;
            text-align: center;
            margin-bottom: 30px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: #2a2f3e;
            border-radius: 8px;
            overflow: hidden;
        }}
        th, td {{
            padding: 14px 16px;
            text-align: left;
            border-bottom: 1px solid #3a4055;
        }}
        th {{
            background: #1f2330;
            color: #a1a1aa;
            font-weight: 600;
            font-size: 0.85em;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        tr:last-child td {{
            border-bottom: none;
        }}
        a {{
            color: #818cf8;
            text-decoration: none;
        }}
        a:hover {{
            color: #a5b4fc;
            text-decoration: underline;
        }}
        .description {{
            color: #a1a1aa;
            line-height: 1.7;
            margin-top: 30px;
            padding: 20px;
            background: #2a2f3e;
            border-radius: 8px;
        }}
        .description strong {{
            color: #e4e4e7;
        }}
        .description ul {{
            margin: 10px 0;
        }}
        .description li {{
            color: #a1a1aa;
        }}
        .links {{
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #3a4055;
            text-align: center;
        }}
        .links a {{
            color: #818cf8;
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
    
    # Generate MkDocs index (without version table)
    index_md = generate_mkdocs_index(versions, current_version)
    
    # Generate standalone version picker (with version table)
    index_html = generate_index_html(versions, current_version)
    
    # Write docs/index.md (for MkDocs navigation - no version table)
    output_path = Path("docs") / "index.md"
    output_path.write_text(index_md, encoding="utf-8")
    
    # Write site/index.html (standalone version picker for root - with version table)
    # This will be copied to site/ after MkDocs build
    site_index_path = Path("site") / "index.html"
    site_index_path.parent.mkdir(parents=True, exist_ok=True)
    site_index_path.write_text(index_html, encoding="utf-8")
    
    print(f"Generated index with {len(versions)} versions: {[v[0] for v in versions]}")


if __name__ == "__main__":
    main()
