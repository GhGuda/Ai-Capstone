# Sprint 0: Planning (Setup)

## Product Vision
The vision of this project is to develop an automated ETL (Extract, Transform, Load) data pipeline that processes the Flight_Price_Dataset_of_Bangladesh.csv by extracting, cleaning, transforming, and loading the data into a structured database while applying Agile and DevOps practices such as CI/CD, testing, and logging.

---

## Project Type
Data Engineering Prototype – Automated ETL Pipeline with CI/CD, Testing, and Monitoring.

---

## Product Backlog (User Stories, Priority & Estimates)

| ID | User Story | Priority | Story Points |
|----|------------|----------|--------------|
| US1 | As a data engineer, I want to extract the raw flight dataset so the pipeline can process real data | High | 3 |
| US2 | As a data engineer, I want to clean and transform the dataset to improve data quality | High | 5 |
| US3 | As a data engineer, I want to load cleaned data into a database for storage and querying | High | 5 |
| US4 | As a developer, I want automated tests to ensure pipeline reliability | Medium | 3 |
| US5 | As a DevOps practitioner, I want a CI/CD pipeline to automate testing on each commit | Medium | 5 |
| US6 | As a user, I want logging and monitoring to track pipeline execution | Low | 2 |

---

## Refined Backlog

### US1: Data Extraction
- System reads CSV dataset successfully
- Dataset loads without runtime errors
- File path is configurable

### US2: Data Transformation
- Missing values handled
- Duplicate records removed
- Column names standardized
- Clean dataset generated

### US3: Data Loading
- Clean data stored in SQLite database
- Table created automatically if not existing
- Data can be queried from database

### US4: Automated Testing
- Unit tests implemented using pytest
- Tests validate extract and transform functions
- Tests run successfully in CI pipeline

### US5: CI/CD Pipeline
- GitHub Actions workflow configured
- Pipeline runs on push and pull request
- Tests executed automatically
- Pipeline fails if tests fail

### US6: Logging & Monitoring
- Pipeline logs saved to pipeline.log
- Errors captured in logs
- Execution stages logged with timestamps

---

## Definition of Done (DoD)
A backlog item is considered Done when:
- Code is implemented and pushed to GitHub
- Acceptance criteria are satisfied
- Unit tests are written and passing
- CI/CD pipeline runs successfully (green build)
- Logging and documentation are updated
- No critical bugs remain
- Commit history shows incremental development (no big-bang commits)

---

## Sprint 1 Plan (Selected Backlog Items)
Selected Stories:
- US1: Data Extraction (3 SP)
- US2: Data Transformation (5 SP)
- US4: Automated Testing (3 SP)

### Sprint Goal
Deliver a working ETL pipeline capable of extracting and transforming the flight dataset with automated testing and CI integration.

---

## System Architecture (Mermaid Diagram)
```mermaid
flowchart LR
    A[Raw Flight Dataset CSV] --> B[Extract Module]
    B --> C[Transform Module]
    C --> D[Cleaned Dataset Output]
    C --> E[SQLite Database]
    B --> F[Unit Tests]
    F --> G[CI/CD Pipeline - GitHub Actions]
