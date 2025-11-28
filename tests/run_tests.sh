#!/bin/bash
# Run all tests for cockpit-design-aesthetics server

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

echo "Running cockpit-design-aesthetics test suite..."
echo ""

if ! command -v pytest &> /dev/null; then
    echo "❌ pytest not found. Install with: pip install pytest pytest-asyncio"
    exit 1
fi

# Run tests with verbose output
python -m pytest tests/test_server.py -v --tb=short

echo ""
echo "✅ Test suite complete!"
