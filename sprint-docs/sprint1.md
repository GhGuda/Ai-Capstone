# Sprint 1: Execution (First Increment)

## Sprint Goal
To deliver the first working increment of the ETL pipeline by implementing data extraction, transformation, automated testing, and CI/CD integration using Agile and DevOps practices.

---

## Backlog Items Completed
- US1: Data Extraction Pipeline
- US2: Data Cleaning & Transformation
- US4: Automated Testing
- US5: CI/CD Pipeline Setup

---

## Work Delivered

### 1. Data Extraction (ETL - Extract Stage)
- Implemented CSV ingestion using Python (Pandas)
- Successfully loaded Flight_Price_Dataset_of_Bangladesh.csv
- Configurable file path support

### 2. Data Transformation (ETL - Transform Stage)
- Removed duplicate records
- Handled missing values
- Standardized column names
- Generated cleaned dataset output

### 3. Automated Testing
- Implemented unit tests using pytest
- Tested extraction and transformation modules
- Integrated tests into CI pipeline

### 4. CI/CD Implementation (DevOps Practice)
- Configured GitHub Actions workflow (main.yml)
- Automated test execution on every push
- Continuous Integration established

---

## Demonstration of Working Software
The ETL pipeline successfully:
- Extracts the raw dataset
- Cleans and transforms the data
- Produces a cleaned CSV file
- Runs automated tests in CI pipeline

Evidence:
- Green CI pipeline status
- Test results (pytest passed)
- Git commit history showing incremental development

---

## Git Delivery Discipline
Development followed incremental commits:
- Initial project setup
- ETL extraction implementation
- Transformation logic added
- Unit tests implemented
- CI/CD pipeline configured

This aligns with Agile iterative delivery and avoids big-bang commits.

---

## Sprint 1 Workflow (Mermaid)
```mermaid
flowchart TD
    A[Git Commit] --> B[GitHub Actions Trigger]
    B --> C[Install Dependencies]
    C --> D[Run Pytest]
    D --> E{Tests Pass?}
    E -->|Yes| F[Successful Build]
    E -->|No| G[Pipeline Fails]
