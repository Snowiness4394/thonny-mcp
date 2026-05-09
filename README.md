# Thonny MCP 🔒🐍

**Your AI Analysis Partner for Private, Local Data Science**

Use AI agents like Claude Desktop or OpenCode CLI to analyze your data **without it ever leaving your computer**. Thonny MCP connects your AI assistant to a clean, isolated Python environment where you maintain complete control.

> *"Your data stays yours. Your AI acts as a collaborative partner, not a service provider."*

---

## 🎯 Who Is This For?

- **Data Analysts** working with sensitive business data
- **Scientists** handling confidential research data  
- **Researchers** with privacy constraints (HIPAA, GDPR, etc.)
- **Students** learning data science with AI guidance
- **Anyone** who wants AI assistance without cloud dependencies

---

## 🔒 Privacy-First Design

| Traditional Cloud Tools | Thonny MCP |
|------------------------|------------|
| ❌ Data uploaded to AI company servers | ✅ **Data never leaves your computer** |
| ❌ Queries logged and analyzed | ✅ **Your analysis is private** |
| ❌ Internet connection required | ✅ **Works completely offline** |
| ❌ Trust required | ✅ **You control everything** |

**Your AI becomes your coding friend and analysis partner - not a data processor.**

---

## ✨ Why Thonny MCP?

**For Data Analysts:**
- 📊 Load CSVs, Excel files, databases - all locally
- 📈 Generate charts and visualizations on your machine
- 🔍 Explore data with pandas, numpy, scipy
- 📉 Run statistical analysis without cloud exposure

**For Scientists:**
- 🧬 Process sensitive research data securely
- 📚 Use specialized libraries (biopython, astropy, etc.)
- 🔬 Reproducible analysis with version-controlled code
- 📝 Generate reports while maintaining data confidentiality

**For Everyone:**
- ✅ **No Python setup headaches** - Thonny just works
- ✅ **Isolated environment** - Won't conflict with system
- ✅ **Open Thonny IDE** - Debug and modify AI-generated code
- ✅ **Install any package** - Full PyPI access via pip

---

## 🚀 Quick Start

### Step 1: Install Thonny (One Time)

1. Visit [https://thonny.org](https://thonny.org)
2. Download `thonny-xx.x.exe` (~30MB)
3. Run installer (takes ~30 seconds)
4. Done! 🎉

### Step 2: Install MCP Server (Inside Thonny)

Open Thonny, then:

**Via Thonny's Shell** (View → Shell or press Ctrl+`):
```python
%pip install thonny-mcp
```

This installs the MCP server **inside Thonny's isolated environment**.

### Step 3: Connect Your AI Assistant

**Find your Thonny Python path:**
In Thonny's Shell, run:
```python
import sys
print(sys.executable)
```

Copy that path (e.g., `C:/Users/You/AppData/Local/Programs/Thonny/python.exe`)

**Configure Claude Desktop:**

Edit `%APPDATA%\Claude\claude_desktop_config.json`:

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

Replace `YOUR_USERNAME` with your Windows username.

**Restart Claude Desktop.** You're ready!

---

## 💡 How It Works

```
You                     AI Agent                Thonny MCP              Your Data
│                           │                       │                       │
│ "Analyze sales.csv"       │                       │                       │
│──────────────────────────>│                       │                       │
│                           │                       │                       │
│                           │  "Load the data"      │                       │
│                           │──────────────────────>│                       │
│                           │                       │                       │
│                           │                       │  Load CSV locally     │
│                           │                       │──────────────────────>│
│                           │                       │                       │
│                           │                       │  Return results       │
│                           │                       │<──────────────────────│
│                           │                       │                       │
│                           │  "Here's what I found"│                       │
│<──────────────────────────│                       │                       │
```

**The AI suggests. You approve. The code runs locally on your machine.**

---

## 🛠️ Available Tools

### `execute(code, timeout=60)`
Run Python code in your isolated Thonny environment.

```python
# Example analysis workflow:
import pandas as pd
import matplotlib.pyplot as plt

# Load your local data
df = pd.read_csv('C:/Users/You/data/sales.csv')

# Explore
print(df.describe())
print(df.head())

# Analyze
correlation = df['price'].corr(df['quantity'])
print(f"Price-Quantity correlation: {correlation}")

# Visualize (saved locally)
plt.scatter(df['price'], df['quantity'])
plt.savefig('C:/Users/You/analysis/output.png')
```

### `install_package(package, upgrade=False)`
Install any Python package you need.

```python
# Install pandas for data analysis
install_package("pandas")

# Install visualization libraries
install_package("matplotlib")
install_package("seaborn")

# Install scientific computing
install_package("numpy")
install_package("scipy")
```

### `list_packages()`
See what's already installed in your environment.

### `save_and_run(script_name, code)`
Save analysis scripts for later reuse.

```python
# Save a reusable analysis script
save_and_run("monthly_report", """
import pandas as pd

# Your analysis code here
df = pd.read_csv('data.csv')
report = df.groupby('month').sum()
print(report)
""")
# Returns: Path to saved file
```

### `open_in_thonny(file_path=None)`
Open Thonny IDE to debug or modify code.

```python
# Open a saved script in Thonny
open_in_thonny("C:/.../thonny/user_scripts/monthly_report.py")
```

**Perfect for:** Understanding what the AI wrote, making tweaks, learning Python!

### `check_thonny_installed()`
Verify everything is set up correctly.

---

## 📊 Example: Private Data Analysis Workflow

```python
# 1. Load your sensitive data (never leaves your machine)
import pandas as pd

df = pd.read_csv('C:/Confidential/customer_data.csv')

# 2. Explore with AI guidance
print(f"Dataset shape: {df.shape}")
print(df.describe())

# 3. Clean data
print("Missing values:", df.isnull().sum())
df_clean = df.dropna()

# 4. Analysis
avg_value = df_clean['purchase_amount'].mean()
print(f"Average purchase: ${avg_value:.2f}")

# 5. Save results locally
results = {
    'total_customers': len(df_clean),
    'avg_purchase': avg_value,
    'top_category': df_clean['category'].mode()[0]
}

import json
with open('C:/Confidential/analysis_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print("✅ Analysis complete. Results saved locally.")
```

**Your data never touched the internet. Your AI helped you think through the analysis.**

---

## 🎓 Learning With AI

Thonny MCP isn't just for analysis - it's a **learning tool**:

1. **Ask AI to explain code** - Get line-by-line explanations
2. **See AI write code** - Learn patterns and best practices  
3. **Open in Thonny** - Step through with the debugger
4. **Modify and experiment** - Safe environment to try things

**Your AI becomes a patient tutor, available 24/7.**

---

## 🔐 Security Best Practices

- ✅ **Keep data on local drives** - Don't use cloud-synced folders for sensitive data
- ✅ **Review AI suggestions** - Understand what code will run before executing
- ✅ **Use Thonny's isolation** - It can't access system files outside its environment
- ✅ **Audit packages** - Only install packages you trust

---

## 🆘 Troubleshooting

### "Thonny not found!"
**Solution:** Install Thonny from https://thonny.org, then restart your AI assistant.

### "Can't find the Python path"
**Solution:** In Thonny's Shell, run:
```python
import sys
print(sys.executable)
```
Copy that exact path into your config.

### "Package installation failed"
**Solution:** Some packages need compilation. Use Thonny's package manager:
**Tools** → **Manage packages...** → Search and install

### "Code execution timeout"
**Solution:** For long-running analysis:
```python
execute("long_analysis_code()", timeout=300)  # 5 minutes
```

---

## 💬 Philosophy

**Thonny MCP is built on these principles:**

1. **Your data is yours** - We help you keep it that way
2. **AI as partner, not replacement** - You maintain control and understanding
3. **Transparency** - See exactly what code runs on your machine
4. **Accessibility** - Data science shouldn't require IT department setup
5. **Education** - Learn while you analyze

---

## 🤝 Contributing

This is a community project to make private data analysis accessible to everyone.

- Found a bug? Open an issue
- Have an idea? Start a discussion
- Want to help? Submit a PR

**Together we can make AI-assisted data science privacy-preserving by default.**

---

## 📄 License

MIT License - Free for personal and commercial use. Keep your data private! 🔒

---

## 🙏 Acknowledgments

- [Thonny](https://thonny.org/) - The Python IDE that makes this possible
- [MCP](https://modelcontextprotocol.io/) - Model Context Protocol by Anthropic
- [FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Python SDK
- The data science community fighting to keep analysis local and private

---

**Analyze freely. Keep data private. Learn continuously.** 🚀🔒📊
