"""
Entry point for running thonny-mcp as a module.

Usage:
    python -m thonny_mcp
    
Or with Thonny:
    C:/Users/You/AppData/Local/Programs/Thonny/python.exe -m thonny_mcp
"""

from thonny_mcp.server import mcp

if __name__ == "__main__":
    mcp.run()
