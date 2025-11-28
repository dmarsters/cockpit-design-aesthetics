#!/bin/bash
# Create standard MCP server project structure for cockpit-design-aesthetics
# Usage: bash create_structure.sh

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_ROOT"

echo "Creating directory structure for cockpit-design-aesthetics..."

# Core directories
mkdir -p src/cockpit_design_aesthetics/ologs
mkdir -p tests/unit
mkdir -p tests/integration
mkdir -p docs

# Create __init__.py files
touch src/cockpit_design_aesthetics/__init__.py
touch tests/__init__.py
touch tests/unit/__init__.py
touch tests/integration/__init__.py

# .gitignore
cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.pytest_cache/
.coverage
htmlcov/
.tox/
.venv
env/
venv/
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store
EOF

# src/cockpit_design_aesthetics/__init__.py
cat > src/cockpit_design_aesthetics/__init__.py << 'EOF'
"""
Cockpit Design Aesthetics MCP Server

Translates cockpit instrument panel design principles into vivid visual language
for image generation using a three-layer categorical architecture.
"""

__version__ = "0.1.0"
EOF

# src/cockpit_design_aesthetics/__main__.py (for local testing)
cat > src/cockpit_design_aesthetics/__main__.py << 'EOF'
"""
Local execution script for Cockpit Design Aesthetics MCP server.

Usage:
    python -m cockpit_design_aesthetics

This runs the server locally for testing and development.
For production, use FastMCP Cloud deployment.
"""

from .server import mcp

if __name__ == "__main__":
    mcp.run()
EOF

# src/cockpit_design_aesthetics/handler.py (for FastMCP Cloud)
cat > src/cockpit_design_aesthetics/handler.py << 'EOF'
"""
FastMCP Cloud entry point for Cockpit Design Aesthetics server.

For FastMCP Cloud deployment, the entry point function must RETURN the server object.
The cloud platform handles the event loop and server.run() call.
"""

from .server import mcp

def handler():
    """Entry point for FastMCP Cloud deployment."""
    return mcp
EOF

# pyproject.toml
cat > pyproject.toml << 'EOF'
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "cockpit-design-aesthetics"
version = "0.1.0"
description = "Cockpit instrument panel design vocabulary MCP server"
readme = "README.md"
requires-python = ">=3.10"
authors = [
    {name = "Dal", email = "dal@lushy.ai"}
]
dependencies = [
    "fastmcp>=0.1.0",
    "pyyaml",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-asyncio>=0.21.0",
]

[project.scripts]
cockpit-design-aesthetics = "cockpit_design_aesthetics.server:mcp"

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages]
find = {where = ["src"]}

[tool.setuptools.package-data]
cockpit_design_aesthetics = ["ologs/*.yaml"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
asyncio_mode = "auto"
EOF

# README.md (brief version)
cat > README.md << 'EOF'
# Cockpit Design Aesthetics MCP Server

Translates cockpit instrument panel design principles into vivid visual language for image generation.

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Test
./tests/run_tests.sh

# Run locally
python -m cockpit_design_aesthetics
```

## Architecture

Three-layer system for cost-optimized image generation:

1. **Layer 1 (Deterministic)**: Instrument taxonomies, positioning rules, color conventions
2. **Layer 2 (Mapping)**: Compose requirements → visual parameters  
3. **Layer 3 (Synthesis)**: Claude generates vivid image prompts

## Tools

- `get_aircraft_type_profile()` - Aircraft configurations
- `get_panel_layout_rules()` - Positioning and grouping logic
- `suggest_instruments()` - Instrument selection for mission
- `build_panel_specification()` - Semantic bridge
- `generate_cockpit_prompt()` - Final image generation prompt

## Documentation

See `docs/DOCUMENTATION.md` for full API reference.
EOF

echo "✅ Directory structure created successfully!"
echo ""
echo "Next steps:"
echo "1. Create server.py (large file - copy manually)"
echo "2. Create test files (large files - copy manually)"
echo "3. Run: ./verify_structure.sh"
echo "4. Run: pip install -e \".[dev]\" from this directory"
echo "5. Run: ./tests/run_tests.sh"
