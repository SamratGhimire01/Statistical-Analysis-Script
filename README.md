# 📊 Statistical Analysis Engine

A professional **CLI tool** to compute descriptive statistics and correlation matrices using **NumPy only**.

It helps analyze numeric datasets for machine learning preprocessing or exploratory data analysis by:

- **Computing** mean, median, and standard deviation from scratch (no SciPy).
- **Calculating** Pearson correlation matrices using a manual covariance formula.
- **Handling** missing values safely with `np.nan_to_num()` and zero-division protection.
- **Supporting** N numeric columns automatically (no hardcoding).
- **Exporting** results to console (formatted table) or JSON (machine-readable).

---

## 🚀 Installation & Setup

1. **Clone the repository** and navigate to the project folder:
   ```bash
   git clone https://github.com/SamratGhimire01/statistical-analysis.git
   cd statistical-analysis


Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📊 Visuals

### Console Output

Formatted statistical report printed to terminal.

![Console Output](images/console_output.png)

### JSON Export

Machine-readable output for API integration or further processing.

![JSON Output](images/json_output.png)

---

## ▶️ Usage

Run the analysis via the terminal:

```bash
python main.py --input data/sample_input.csv --output data/result.json --format json
```

---

## ⚙️ Command Arguments

| Argument   | Description                                                                                |
| ---------- | ------------------------------------------------------------------------------------------ |
| `--input`  | **Required**: Path to the source CSV file (must have header row)                           |
| `--output` | Path where results will be saved (Default: `data/sample_output.json`)                      |
| `--format` | Output format: `console` (formatted table) or `json` (structured data). Default: `console` |

---

## 💡 Example

```bash
# Full analysis with JSON export:
python main.py \
--input data/traffic_data.csv \
--output results/traffic_stats.json \
--format json
```

```bash
# Quick console report:
python main.py --input data/health_data.csv --format console
```

```bash
# Custom output path:
python main.py --input data.csv --output reports/summary.json --format json
```

---

## 📐 Mathematical Formulas

This tool implements statistics from scratch to build intuition:

| Metric          | Formula                    | Implementation                              |
| --------------- | -------------------------- | ------------------------------------------- |
| **Mean**        | μ = (1/n) Σ xᵢ             | `np.sum(data, axis=0) / n`                  |
| **Median**      | Middle value (sorted)      | Custom `medians()` with odd/even logic      |
| **Std Dev**     | σ = √[ (1/n) Σ (xᵢ - μ)² ] | `np.sqrt(np.mean((data - mean)**2))`        |
| **Correlation** | ρ = cov(X,Y) / (σₓ · σᵧ)   | `((X-μₓ)ᵀ @ (Y-μᵧ) / n) / np.outer(σₓ, σᵧ)` |

---

## ⚠️ NaN Handling Policy

* Columns with **all NaN** values are removed automatically.
* Columns with **some NaN** values are kept; correlation uses `np.nan_to_num()` to replace undefined results with `0.0`.
* To change this behavior, edit `src/loader.py`.

---

## 🧪 Testing

Verify the statistical logic using the built-in test suite:

```bash
pytest tests/test_stats.py
```

**Test Coverage:**

* ✅ Mean/median/std calculation for known data
* ✅ Median correctness for odd/even row counts
* ✅ Zero-variance (constant column) safety
* ✅ Perfect correlation detection (r = 1.0)

---

## 📁 Project Structure

```
statistical-analysis/
├── main.py
├── src/
│   ├── cli.py
│   ├── loader.py
│   ├── stats.py
│   ├── reporter.py
│   └── log.py
├── tests/
│   └── test_stats.py
├── data/
│   ├── sample_input.csv
│   └── sample_output.json
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Author

**Samrat Ghimire**
GitHub: [https://github.com/SamratGhimire01/Statistical-Analysis-Script.git]

LinkedIn: *[(https://www.linkedin.com/in/samratghimire01/)]*

---

