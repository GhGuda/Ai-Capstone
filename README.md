# Flight ETL Data Pipeline (Agile + DevOps Prototype)

## Project Overview
This project is a Data Engineering ETL pipeline developed using Agile and DevOps practices.  
The pipeline extracts raw flight price data, transforms and cleans the dataset, and outputs a processed dataset ready for analysis.

This prototype was developed over multiple sprints with CI/CD integration, automated testing, and incremental Git commits to demonstrate Agile delivery and DevOps discipline.

---

## Product Vision
To build an automated ETL data pipeline that extracts, cleans, and processes flight price data using Python while integrating CI/CD and automated testing to ensure reliability and continuous delivery.

---

## Tech Stack
- Python (Pandas)
- Pytest (Testing)
- Git & GitHub (Version Control)
- GitHub Actions (CI/CD Pipeline)

---

## Project Structure

```bash
agile-lab/
│
├── raw_bangladesh_data/
│ ├── Flight_Price_Dataset_of_Bangladesh.csv
│ └── cleaned_flight_data.csv
│
├── src/
│ ├── extract.py
│ ├── transform.py
│ └── pipeline.py
│
├── tests/
│ └── test_pipeline.py
│
├── requirements.txt
└── .github/workflows/main.yml
```

---

## ETL Pipeline Workflow
1. Extract raw CSV dataset
2. Clean and transform data (remove duplicates, handle missing values)
3. Save cleaned dataset for analysis
4. Run automated tests via CI pipeline

---

## How to Run the Pipeline
```bash
pip install -r requirements.txt
python src/pipeline.py
```

Testing

Unit tests are implemented using Pytest to validate:

- Data extraction

- Data transformation

- Data quality checks

Run tests locally:

- pytest


CI/CD Integration (DevOps)

A GitHub Actions CI pipeline is configured to:

- Automatically run on every push

- Install dependencies

- Execute unit tests

- Detect failures early

Pipeline file location:

- .github/workflows/main.yml