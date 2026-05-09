# Thonny MCP 🔒🐍

**Your AI Analysis Partner for Private, Local Data Science**

Use AI agents to analyze your data **without it ever leaving your computer**. Thonny MCP connects your AI assistant to a clean, isolated Python environment where you maintain complete control.

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

### Alternative - OpenCode CLI (Recommended for Privacy!)

**[OpenCode CLI](https://github.com/anomalyco/opencode)** is a fantastic choice for private, local AI assistance:

1. **Install OpenCode CLI:**
   ```bash
   npm install -g @opencode/cli
   ```

2. **Get OpenCode Go (cheap & effective):**
   - Visit [OpenCode pricing](https://opencode.ai/pricing)
   - **Go plan** offers affordable access to powerful AI models
   - Perfect for data analysis workloads
   - Private and secure

3. **Configure OpenCode with Thonny MCP:**
   
   Create `.opencode/mcp.json` in your project folder:
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

4. **Start analyzing:**
   ```bash
   opencode
   ```

**Why OpenCode CLI + Go Plan?**
- 💰 **Affordable** - Much cheaper than other AI services
- 🔒 **Private** - Your data stays local
- ⚡ **Fast** - Direct connection to your Thonny environment
- 🎯 **Focused** - Purpose-built for coding and analysis

---

## 💡 How It Works

```
You                     AI Agent (Claude/OpenCode)      Thonny MCP              Your Data
│                               │                               │                       │
│ "Analyze this CSV for me"     │                               │                       │
│───────────────────────────────>│                               │                       │
│                               │                               │                       │
│                               │  "I'll load it with pandas"   │                       │
│                               │──────────────────────────────>│                       │
│                               │                               │                       │
│                               │                               │  Load CSV locally     │
│                               │                               │──────────────────────>│
│                               │                               │                       │
│                               │                               │  Return results       │
│                               │                               │<──────────────────────│
│                               │                               │                       │
│                               │  "Found interesting patterns" │                       │
│<───────────────────────────────│                               │                       │
```

**The AI suggests. You approve. The code runs locally on your machine.**

---

## 📊 Real-World Example: NYC Taxi Data Analysis

Here's exactly how you'd work with your AI agent to analyze real data:

### **Step 0: Install Required Packages**

**You:** *"I want to analyze some data with pandas. Do I need to install anything?"*

**AI Agent:**
*"Yes! Let me install the required packages for data analysis:"

```python
# Install required packages
install_package("pandas")
install_package("pyarrow")  # For reading parquet files
install_package("matplotlib")
install_package("numpy")
```

**AI:** *"✅ Packages installed! Now we can work with data."

---

### **Step 1: Download Data**

**You:** *"Let's analyze NYC taxi data. Can you download the January 2023 dataset from the NYC TLC website?"*

**AI Agent (via Thonny MCP):**
```python
import urllib.request
import os

# Create data directory
data_dir = "C:/Users/You/data_analysis/nyc_taxi"
os.makedirs(data_dir, exist_ok=True)

# Download NYC taxi data (January 2023)
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
file_path = os.path.join(data_dir, "yellow_tripdata_2023-01.parquet")

print(f"Downloading from {url}...")
urllib.request.urlretrieve(url, file_path)
print(f"✅ Downloaded to {file_path}")
print(f"File size: {os.path.getsize(file_path) / (1024*1024):.1f} MB")
```

### **Step 2: Explore the Data**

**You:** *"Great! Now let's explore what's in this dataset."*

**AI Agent:**
```python
import pandas as pd

# Load the data
df = pd.read_parquet("C:/Users/You/data_analysis/nyc_taxi/yellow_tripdata_2023-01.parquet")

print(f"Dataset shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
print("\nColumn names:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head())
```

**AI responds:** *"The dataset has 3,066,766 taxi trips with 19 columns including pickup/dropoff times, passenger counts, trip distances, and fares."*

### **Step 3: Data Quality Check**

**You:** *"Are there any data quality issues we should know about?"*

**AI Agent:**
```python
print("=== Data Quality Report ===\n")

# Check for missing values
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
print("Missing values:")
print(missing[missing > 0])
print()

# Check data types
print("Data types:")
print(df.dtypes)
print()

# Basic statistics for numeric columns
print("Numeric columns summary:")
print(df.describe())
```

### **Step 4: Analysis** 

**You:** *"What's the average trip distance and fare? Any patterns by time of day?"*

**AI Agent:**
```python
import matplotlib.pyplot as plt
import numpy as np

# Calculate trip duration in minutes
df['trip_duration'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60

# Filter out obvious outliers
df_clean = df[
    (df['trip_distance'] > 0) & 
    (df['trip_distance'] < 100) &  # Less than 100 miles
    (df['fare_amount'] > 0) &
    (df['fare_amount'] < 500) &    # Less than $500
    (df['trip_duration'] > 0) &
    (df['trip_duration'] < 180)     # Less than 3 hours
].copy()

print(f"Cleaned dataset: {len(df_clean):,} trips (removed {len(df) - len(df_clean):,} outliers)")
print()

# Key metrics
print("=== Key Metrics ===")
print(f"Average trip distance: {df_clean['trip_distance'].mean():.2f} miles")
print(f"Average fare: ${df_clean['fare_amount'].mean():.2f}")
print(f"Average trip duration: {df_clean['trip_duration'].mean():.1f} minutes")
print(f"Average speed: {(df_clean['trip_distance'] / (df_clean['trip_duration']/60)).mean():.1f} mph")
print()

# Extract hour for time-of-day analysis
df_clean['pickup_hour'] = df_clean['tpep_pickup_datetime'].dt.hour

# Trips by hour
hourly_trips = df_clean.groupby('pickup_hour').size()
print("=== Trips by Hour of Day ===")
for hour, count in hourly_trips.items():
    bar = "█" * int(count / hourly_trips.max() * 30)
    print(f"{hour:2d}:00 {bar} {count:,}")
```

### **Step 5: Visualization**

**You:** *"Can you create some visualizations and save them locally?"*

**AI Agent:**
```python
# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Trips by hour
hourly_trips.plot(kind='bar', ax=axes[0,0], color='steelblue')
axes[0,0].set_title('NYC Taxi Trips by Hour of Day (January 2023)')
axes[0,0].set_xlabel('Hour')
axes[0,0].set_ylabel('Number of Trips')
axes[0,0].tick_params(axis='x', rotation=0)

# 2. Trip distance distribution
axes[0,1].hist(df_clean['trip_distance'], bins=50, color='coral', edgecolor='black')
axes[0,1].set_title('Distribution of Trip Distances')
axes[0,1].set_xlabel('Distance (miles)')
axes[0,1].set_ylabel('Frequency')
axes[0,1].set_xlim(0, 20)

# 3. Fare vs Distance scatter
sample = df_clean.sample(n=5000)  # Sample for performance
axes[1,0].scatter(sample['trip_distance'], sample['fare_amount'], alpha=0.5, s=1)
axes[1,0].set_title('Fare Amount vs Trip Distance')
axes[1,0].set_xlabel('Trip Distance (miles)')
axes[1,0].set_ylabel('Fare Amount ($)')
axes[1,0].set_xlim(0, 25)
axes[1,0].set_ylim(0, 100)

# 4. Payment type distribution
payment_counts = df_clean['payment_type'].value_counts()
payment_labels = {1: 'Credit Card', 2: 'Cash', 3: 'No Charge', 4: 'Dispute', 5: 'Unknown'}
payment_counts.index = payment_counts.index.map(payment_labels)
axes[1,1].pie(payment_counts.values, labels=payment_counts.index, autopct='%1.1f%%')
axes[1,1].set_title('Payment Type Distribution')

plt.tight_layout()

# Save locally
output_path = "C:/Users/You/data_analysis/nyc_taxi/analysis.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"✅ Visualization saved to: {output_path}")

# Show correlation
correlation = df_clean['trip_distance'].corr(df_clean['fare_amount'])
print(f"\nCorrelation between distance and fare: {correlation:.3f}")
```

### **Step 6: Insights Summary**

**AI Agent provides summary:**

*"Based on the analysis of 3+ million NYC taxi trips in January 2023:***

1. **Peak Hours:** 6-8 PM sees the highest volume (~200k trips/hour)
2. **Average Trip:** 3.1 miles, $18.42 fare, 16 minutes
3. **Payment:** 72% use credit cards, 23% cash
4. **Outliers:** Removed 45k trips with unrealistic distances/fares
5. **Correlation:** Strong correlation (0.87) between distance and fare

*The visualizations are saved locally for your reference."*

---

## 🎓 Learning With AI

**You:** *"I don't understand this pandas groupby function. Can you explain?"*

**AI Agent:**
*"Sure! `groupby()` is like creating buckets for your data. Let me show you with our taxi data:"*

```python
# Simple explanation with example
print("Grouping by pickup hour and calculating averages:")

hourly_stats = df_clean.groupby('pickup_hour').agg({
    'fare_amount': 'mean',
    'trip_distance': 'mean',
    'passenger_count': 'sum'
}).round(2)

print(hourly_stats.head(10))

print("\nThink of it like this:")
print("- groupby('pickup_hour') = 'Put all trips from 9 AM in one bucket'")
print("- .agg({...}) = 'For each bucket, calculate these statistics'")
print("- Result = One row per hour with your calculated values")
```

**You:** *"Can you open this in Thonny so I can play with it?"*

**AI Agent:**
```python
# Save the analysis script
save_and_run("nyc_taxi_analysis", """
# NYC Taxi Analysis - Complete Script
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_parquet("C:/Users/You/data_analysis/nyc_taxi/yellow_tripdata_2023-01.parquet")

# Add your exploration code here!
print(f"Loaded {len(df):,} trips")
print(df.head())
""")

# Now open in Thonny
open_in_thonny("C:/Users/You/AppData/Local/Programs/Thonny/user_scripts/nyc_taxi_analysis.py")
```

**Now you can step through the code in Thonny's debugger, modify it, and learn!**

---

## 🛠️ Available Tools

### `execute(code, timeout=60)`
Run Python code in your isolated Thonny environment.

### `install_package(package, upgrade=False)`
Install any Python package you need.

```python
# Install analysis libraries
install_package("pandas")
install_package("matplotlib")
install_package("seaborn")
install_package("numpy")
install_package("pyarrow")  # For parquet files
```

### `list_packages()`
See what's already installed.

### `save_and_run(script_name, code)`
Save analysis scripts for later reuse.

### `open_in_thonny(file_path=None)`
Open Thonny IDE to debug or modify code.

### `check_thonny_installed()`
Verify everything is set up correctly.

---

## 🔐 Security Best Practices

- ✅ **Keep data on local drives** - Don't use cloud-synced folders for sensitive data
- ✅ **Review AI suggestions** - Understand what code will run before executing
- ✅ **Use Thonny's isolation** - It can't access system files outside its environment
- ✅ **Audit packages** - Only install packages you trust
- ✅ **Delete when done** - Clean up downloaded data files after analysis

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
- [OpenCode](https://opencode.ai/) - Affordable, private AI for developers
- NYC Taxi & Limousine Commission - For the excellent public dataset
- The data science community fighting to keep analysis local and private

---

**Analyze freely. Keep data private. Learn continuously.** 🚀🔒📊
