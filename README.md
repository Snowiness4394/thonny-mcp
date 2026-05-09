# Thonny MCP 🐍

**Execute Python code via [Thonny](https://thonny.org/)'s isolated environment from AI agents.**

Perfect for data analysts, scientists, and anyone who wants a clean, working Python setup on Windows without the headaches!

---

## ✨ Why Thonny MCP?

| Problem | Solution |
|---------|----------|
| ❌ Windows doesn't have Python pre-installed | ✅ Just install Thonny (one download) |
| ❌ PATH issues, permission problems | ✅ Thonny is completely isolated |
| ❌ Multiple Python versions conflicting | ✅ One clean environment |
| ❌ Can't debug AI-generated code | ✅ Open any script in Thonny's IDE! |
| ❌ Package management is confusing | ✅ Simple pip install via MCP |

---

## 🚀 Quick Start

### Step 1: Install Thonny (One Time)

1. Visit [https://thonny.org](https://thonny.org)
2. Download `thonny-xx.x.exe`
3. Run the installer (takes ~30 seconds)
4. Done! 🎉

### Step 2: Install This MCP Server (Inside Thonny!)

Open Thonny, then:

**Option A: Via Thonny's GUI**
1. Go to **Tools** → **Manage packages...**
2. Search for `thonny-mcp`
3. Click **Install**

**Option B: Via Thonny's Shell**
```bash
# Open Thonny, then open the Shell (View → Shell)
# Or press Ctrl+` (backtick)

# Then run:
%pip install thonny-mcp
```

This installs `thonny-mcp` **inside Thonny's isolated environment**, keeping everything clean!

### Step 3: Configure Your AI Assistant

**Important:** Use the full path to Thonny's Python to run the MCP server:

**Claude Desktop:**

Add to `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "thonny-python": {
      "command": "C:/Users/YOUR_USERNAME/AppData/Local/Programs/Thonny/python.exe",
      "args": ["-m", "thonny_mcp.server"]
    }
  }
}
```

**Cursor:**

Add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "thonny-python": {
      "command": "C:/Users/YOUR_USERNAME/AppData/Local/Programs/Thonny/python.exe",
      "args": ["-m", "thonny_mcp.server"]
    }
  }
}
```

**Windsurf:**

Add to `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "thonny-python": {
      "command": "C:/Users/YOUR_USERNAME/AppData/Local/Programs/Thonny/python.exe",
      "args": ["-m", "thonny_mcp.server"]
    }
  }
}
```

**💡 Pro Tip:** The path follows this pattern:
- `C:/Users/[YOUR_USERNAME]/AppData/Local/Programs/Thonny/python.exe`

Just replace `YOUR_USERNAME` with your Windows username!

**🔍 Finding Your Exact Path:**

Open Thonny and go to **Tools** → **Open system shell...**, then type:
```bash
where python
```

Or in Thonny's Shell (View → Shell):
```python
import sys
print(sys.executable)
```

Copy that path and use it in your config!

Restart your AI assistant and you're ready to go!

---

## 🛠️ Available Tools

### `execute(code, timeout=60)`
Run Python code in Thonny's environment.

```python
# Example: Your AI assistant can execute:
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
print(df.describe())
```

### `install_package(package, upgrade=False)`
Install packages using pip.

```python
# Install pandas
install_package("pandas")

# Upgrade numpy
install_package("numpy", upgrade=True)
```

### `list_packages()`
See what's installed.

### `get_environment_info()`
Check Python version and paths.

### `save_and_run(script_name, code)`
Save code to a file and execute it.

```python
# Save analysis.py and run it
save_and_run("analysis", "import pandas as pd; ...")
# Returns: file path for later use!
```

### `open_in_thonny(file_path=None)`
Open Thonny IDE - great for debugging!

```python
# Open a saved script in Thonny's GUI
open_in_thonny("C:/.../thonny/user_scripts/analysis.py")
```

### `check_thonny_installed()`
Verify Thonny is accessible.

---

## 📊 Perfect For Data Analysis

### Example Workflow with DuckDB

```python
# Your AI assistant writes:
import duckdb
import pandas as pd

# Connect to your database
conn = duckdb.connect('C:/data/sales.db')

# Query
df = conn.execute("""
    SELECT 
        region,
        SUM(revenue) as total_revenue,
        AVG(units) as avg_units
    FROM sales
    WHERE date >= '2024-01-01'
    GROUP BY region
""").df()

# Process in Python
df['growth'] = df['total_revenue'].pct_change()
print(df.sort_values('total_revenue', ascending=False))
```

### Install Analysis Libraries

```python
install_package("pandas")
install_package("numpy") 
install_package("matplotlib")
install_package("duckdb")
install_package("jupyter")
```

---

## 🔧 Troubleshooting

### "Thonny not found!"

**Solution:** Install Thonny from https://thonny.org, then restart your AI assistant.

### "Package installation failed"

**Solution:** Some packages need compilation. Try:
```python
install_package("package-name", upgrade=True)
```

Or open Thonny and use its package manager (Tools > Manage Packages).

### "Code execution timeout"

**Solution:** Increase timeout:
```python
execute("long_running_code()", timeout=300)  # 5 minutes
```

---

## 🎯 Windows Only? Yes, Intentionally!

Linux and macOS already have Python in the terminal. This is specifically for Windows users who want a frictionless Python experience!

---

## 🤝 Contributing

Contributions welcome! This is a community project to make Python accessible for AI-assisted data analysis.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

MIT License - feel free to use in personal and commercial projects!

---

## 🙏 Acknowledgments

- [Thonny](https://thonny.org/) - The fantastic Python IDE for beginners
- [MCP](https://modelcontextprotocol.io/) - Model Context Protocol by Anthropic
- [FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Python SDK for MCP

---

## 💡 Pro Tips

1. **Save your scripts** - Use `save_and_run()` so you can open them in Thonny later
2. **Check installed packages** - Use `list_packages()` to see what's available
3. **Debug in Thonny** - Use `open_in_thonny()` to debug AI-generated code
4. **Combine with DuckDB** - Thonny + DuckDB = perfect for local data analysis

---

**Happy analyzing! 🚀📊**
