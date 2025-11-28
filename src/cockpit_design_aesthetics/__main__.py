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
