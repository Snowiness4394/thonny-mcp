"""
Thonny MCP Server

Execute Python code using Thonny's isolated environment.
Designed for Windows users who want a clean, working Python setup.
"""

from mcp.server.fastmcp import FastMCP
import subprocess
import sys
import os
from pathlib import Path
from typing import Optional
import json

# Create MCP server instance
mcp = FastMCP("ThonnyPython")


def find_thonny_python() -> Optional[Path]:
    """
    Find Thonny's Python executable on Windows.
    
    Checks common installation locations in order:
    1. User install (AppData/Local)
    2. Program Files
    3. Program Files (x86)
    4. Portable installs (C:/Thonny)
    5. Custom user path (~/Thonny)
    
    Returns:
        Path to python.exe if found, None otherwise
    """
    possible_paths = [
        # User install (most common)
        Path.home() / "AppData/Local/Programs/Thonny/python.exe",
        # System-wide install
        Path("C:/Program Files/Thonny/python.exe"),
        # 32-bit system install
        Path("C:/Program Files (x86)/Thonny/python.exe"),
        # Portable install
        Path("C:/Thonny/python.exe"),
        # Custom user path
        Path.home() / "Thonny/python.exe",
    ]
    
    for path in possible_paths:
        if path.exists():
            return path
    
    return None


def get_python_exe() -> str:
    """
    Get Thonny's Python executable path.
    
    Returns:
        String path to Python executable
        
    Raises:
        RuntimeError: If Thonny is not found
    """
    thonny_python = find_thonny_python()
    
    if thonny_python:
        return str(thonny_python)
    
    # Helpful error message with installation instructions
    raise RuntimeError(
        "❌ Thonny not found!\n\n"
        "Please install Thonny (it's free and takes 30 seconds):\n"
        "1. Visit: https://thonny.org\n"
        "2. Download: thonny-xx.x.exe\n"
        "3. Run the installer\n"
        "4. Restart your AI assistant\n\n"
        "Thonny provides an isolated Python environment\n"
        "that's perfect for AI agents and data analysis!"
    )


# Cache the Python path at module load
PYTHON_EXE = get_python_exe()


@mcp.tool()
def execute(code: str, timeout: int = 60) -> dict:
    """
    Execute Python code in Thonny's isolated environment.
    
    Args:
        code: Python code to execute
        timeout: Maximum execution time in seconds (default: 60)
    
    Returns:
        Dictionary containing:
        - stdout: Standard output from the code
        - stderr: Standard error from the code  
        - returncode: Exit code (0 = success)
        - success: Boolean indicating if execution succeeded
    
    Example:
        execute("print('Hello World')")
        execute("import pandas as pd; df = pd.DataFrame(); print(df)")
    """
    try:
        result = subprocess.run(
            [PYTHON_EXE, "-c", code],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
            "success": result.returncode == 0
        }
    except subprocess.TimeoutExpired:
        return {
            "stdout": "",
            "stderr": f"⏱️ Execution timed out after {timeout} seconds",
            "returncode": -1,
            "success": False
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": f"❌ Error: {str(e)}",
            "returncode": -1,
            "success": False
        }


@mcp.tool()
def install_package(package: str, upgrade: bool = False) -> dict:
    """
    Install a Python package using Thonny's pip.
    
    Args:
        package: Package name (e.g., 'pandas', 'requests', 'numpy')
        upgrade: Whether to upgrade if already installed (default: False)
    
    Returns:
        Dictionary containing installation result
    
    Example:
        install_package("pandas")
        install_package("requests", upgrade=True)
    """
    cmd = [PYTHON_EXE, "-m", "pip", "install"]
    if upgrade:
        cmd.append("--upgrade")
    cmd.append(package)
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120  # Package installs can take time
        )
        
        # Parse output for user-friendly message
        if result.returncode == 0:
            message = f"✅ Successfully installed {package}"
        else:
            message = f"❌ Failed to install {package}"
        
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "message": message,
            "success": result.returncode == 0
        }
    except subprocess.TimeoutExpired:
        return {
            "stdout": "",
            "stderr": "",
            "message": f"⏱️ Installation of {package} timed out",
            "success": False
        }


@mcp.tool()
def list_packages() -> list:
    """
    List all packages installed in Thonny's environment.
    
    Returns:
        List of dictionaries with 'name' and 'version' keys
        
    Example:
        [
            {"name": "pandas", "version": "2.0.0"},
            {"name": "numpy", "version": "1.24.0"}
        ]
    """
    try:
        result = subprocess.run(
            [PYTHON_EXE, "-m", "pip", "list", "--format=json"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            packages = json.loads(result.stdout)
            return packages
        else:
            return []
    except Exception:
        return []


@mcp.tool()
def get_environment_info() -> dict:
    """
    Get information about the Thonny Python environment.
    
    Returns:
        Dictionary containing:
        - python_version: Python version string
        - pip_version: Pip version string
        - thonny_path: Directory where Thonny is installed
        - python_executable: Full path to python.exe
    """
    info = {
        "python_version": "Unknown",
        "pip_version": "Unknown", 
        "thonny_path": str(Path(PYTHON_EXE).parent),
        "python_executable": PYTHON_EXE
    }
    
    # Get Python version
    try:
        result = subprocess.run(
            [PYTHON_EXE, "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            info["python_version"] = result.stdout.strip()
    except:
        pass
    
    # Get pip version
    try:
        result = subprocess.run(
            [PYTHON_EXE, "-m", "pip", "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            info["pip_version"] = result.stdout.strip()
    except:
        pass
    
    return info


@mcp.tool()
def open_in_thonny(file_path: Optional[str] = None) -> dict:
    """
    Open the Thonny IDE.
    
    Optionally open a specific Python file. This is great for
    debugging or modifying scripts generated by AI agents!
    
    Args:
        file_path: Optional path to a .py file to open
    
    Returns:
        Dictionary with success status and message
    
    Example:
        open_in_thonny()  # Just open Thonny
        open_in_thonny("C:/Users/Me/analysis.py")  # Open specific file
    """
    thonny_exe = Path(PYTHON_EXE).parent / "thonny.exe"
    
    if not thonny_exe.exists():
        return {
            "success": False,
            "message": "❌ Thonny IDE executable not found"
        }
    
    try:
        if file_path and Path(file_path).exists():
            subprocess.Popen([str(thonny_exe), file_path])
            message = f"✅ Opened Thonny with {file_path}"
        else:
            subprocess.Popen([str(thonny_exe)])
            message = "✅ Opened Thonny IDE"
        
        return {
            "success": True,
            "message": message
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"❌ Error opening Thonny: {str(e)}"
        }


@mcp.tool()
def save_and_run(script_name: str, code: str) -> dict:
    """
    Save code to a file and execute it.
    
    This is useful for longer scripts that you might want to
    revisit later or modify in Thonny's IDE.
    
    Args:
        script_name: Name for the script (without .py extension)
        code: Python code to save and run
    
    Returns:
        Dictionary with execution results and file path
    
    Example:
        save_and_run("analysis", "import pandas as pd; print(pd.__version__)")
    """
    # Create a scripts directory in Thonny's folder
    thonny_dir = Path(PYTHON_EXE).parent
    scripts_dir = thonny_dir / "user_scripts"
    scripts_dir.mkdir(exist_ok=True)
    
    # Ensure .py extension
    if not script_name.endswith('.py'):
        script_name += '.py'
    
    script_path = scripts_dir / script_name
    
    try:
        # Write the script
        script_path.write_text(code, encoding='utf-8')
        
        # Execute the file
        result = subprocess.run(
            [PYTHON_EXE, str(script_path)],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        return {
            "file_saved": str(script_path),
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
            "success": result.returncode == 0,
            "hint": f"💡 Open in Thonny: open_in_thonny({str(script_path)})"
        }
    except subprocess.TimeoutExpired:
        return {
            "file_saved": str(script_path),
            "stdout": "",
            "stderr": "⏱️ Execution timed out",
            "returncode": -1,
            "success": False
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@mcp.tool()
def check_thonny_installed() -> dict:
    """
    Check if Thonny is installed and accessible.
    
    Returns:
        Dictionary with installation status and path if found
    """
    thonny_path = find_thonny_python()
    
    if thonny_path:
        return {
            "installed": True,
            "python_path": str(thonny_path),
            "message": "✅ Thonny found! Ready to execute Python code."
        }
    else:
        return {
            "installed": False,
            "python_path": None,
            "message": (
                "❌ Thonny not found.\n\n"
                "Install from https://thonny.org\n"
                "Then restart your AI assistant."
            )
        }


if __name__ == "__main__":
    # Start the MCP server
    print(f"🚀 Starting Thonny MCP Server...")
    print(f"📍 Using Python: {PYTHON_EXE}")
    mcp.run()
