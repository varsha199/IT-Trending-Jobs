# 🚀 IT Job Trends Analysis (LinkedIn Job Postings)

Explore how the IT job market is evolving by analyzing LinkedIn job postings.  
We track **job role trends**, **in-demand skills**, **salary distributions**, and **location-based demand** using real-world data.

[📊 Dataset on Kaggle](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)

---

## 🎯 Project Objectives

- 🔍 Identify **trending and declining IT roles** over time
- 🧠 Discover the **most in-demand skills** (e.g., Python, AWS, SQL)
- 💰 Compare **salary ranges** by job title and geography
- 📍 Highlight **hotspots** for tech job demand

---

## 📁 Project Structure

```
IT-TRENDING-JOBS/
│
├── notebooks/
│   ├── 1_data_load.ipynb        ← Load & inspect data
│   ├── 2_data_cleaning.ipynb    ← Clean missing/dirty data
│   └── 3_data_analysis.ipynb    ← Analyze roles, skills, salaries
│
├── scripts/
│   └── functions.py             ← Utility functions for reuse
│
├── main.ipynb                   ← Master pipeline notebook
├── .gitignore                   ← Ignore checkpoints, venv, etc.
├── README.md                    ← Project overview & usage
└── requirements.txt             ← Project dependencies
```

---

## 📝 Notebooks Breakdown

| Notebook | Purpose |
|----------|---------|
| `1_data_load.ipynb` | Loads and previews the dataset |
| `2_data_cleaning.ipynb` | Fixes missing values, cleans salary & skills columns |
| `3_data_analysis.ipynb` | Creates visualizations for trends and insights |
| `main.ipynb` | Runs the full project pipeline for reporting |

---

## 🔧 Setup Instructions

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/IT-TRENDING-JOBS.git
cd IT-TRENDING-JOBS
```

**2. (Optional) Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Launch Jupyter Notebook**
```bash
jupyter notebook
```

---

## 📊 Sample Visuals (Planned)

- 📈 **Time-series plots** of job postings by category (monthly/quarterly)
- 🧠 **Top 10 in-demand skills**
- 💰 **Salary distribution** by city and role
- 🌍 **Location heatmaps** showing tech job demand

---

## 📦 Dataset Info

**Source:** [Kaggle – LinkedIn Job Postings](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)  
**File Used:** `postings.csv`

**Key Columns:**
- `job_title`
- `location`
- `company`
- `posted_date`
- `salary_range`
- `skills`
- `description`

---

## 🙋 Author

**Your Name**  
GitHub: [@varsha199](https://github.com/varsha199/IT-Trending-Jobs)

---

## 📄 License

This project is licensed under the **MIT License**.  
Feel free to use, fork, or contribute!
