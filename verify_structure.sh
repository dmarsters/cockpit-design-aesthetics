#!/bin/bash
# Verify project structure matches standards

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_ROOT"

echo "Verifying cockpit-design-aesthetics project structure..."
echo ""

ERRORS=0

# Check critical files exist
check_file() {
    if [ -f "$1" ]; then
        echo "✅ $1"
    else
        echo "❌ MISSING: $1"
        ERRORS=$((ERRORS + 1))
    fi
}

# Check critical directories exist
check_dir() {
    if [ -d "$1" ]; then
        echo "✅ $1/"
    else
        echo "❌ MISSING: $1/"
        ERRORS=$((ERRORS + 1))
    fi
}

echo "=== Root Level Files ==="
check_file "pyproject.toml"
check_file "README.md"
check_file ".gitignore"
check_file "create_structure.sh"
check_file "verify_structure.sh"

echo ""
echo "=== Directories ==="
check_dir "src/cockpit_design_aesthetics"
check_dir "src/cockpit_design_aesthetics/ologs"
check_dir "tests"
check_dir "tests/unit"
check_dir "tests/integration"
check_dir "docs"

echo ""
echo "=== Package Files ==="
check_file "src/cockpit_design_aesthetics/__init__.py"
check_file "src/cockpit_design_aesthetics/__main__.py"
check_file "src/cockpit_design_aesthetics/handler.py"
check_file "tests/__init__.py"
check_file "tests/unit/__init__.py"
check_file "tests/integration/__init__.py"

echo ""
echo "=== Pending (Create Manually) ==="
if [ ! -f "src/cockpit_design_aesthetics/server.py" ]; then
    echo "⏳ src/cockpit_design_aesthetics/server.py (LARGE FILE - copy manually)"
else
    echo "✅ src/cockpit_design_aesthetics/server.py"
fi

if [ ! -f "src/cockpit_design_aesthetics/ologs/instruments.yaml" ]; then
    echo "⏳ src/cockpit_design_aesthetics/ologs/instruments.yaml (OLOG - create manually)"
else
    echo "✅ src/cockpit_design_aesthetics/ologs/instruments.yaml"
fi

if [ ! -f "tests/run_tests.sh" ]; then
    echo "⏳ tests/run_tests.sh (create manually)"
else
    echo "✅ tests/run_tests.sh"
fi

if [ ! -f "tests/test_server.py" ]; then
    echo "⏳ tests/test_server.py (LARGE FILE - copy manually)"
else
    echo "✅ tests/test_server.py"
fi

echo ""
if [ $ERRORS -eq 0 ]; then
    echo "✅ Core structure verified successfully!"
    echo ""
    echo "Next: Create server.py, ologs, and test files"
else
    echo "❌ Found $ERRORS structural issues"
    exit 1
fi
