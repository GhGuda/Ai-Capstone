# Sprint 2: Execution & Improvement

## Sprint Goal
To apply feedback from Sprint 1 and enhance the ETL pipeline by implementing database loading, logging/monitoring, CI stability fixes, and improved testing.

---

## Feedback Applied from Sprint 1 Retrospective
- Improve test coverage and reliability
- Implement full ETL lifecycle (Load stage)
- Add monitoring and logging
- Fix CI/CD module import issues

---

## Backlog Items Completed in Sprint 2
- US3: Load Data into Database
- US6: Logging and Monitoring
- CI/CD Stability Improvements
- Enhanced Test Coverage

---

## New Features Delivered

### 1. Full ETL Implementation (Load Stage)
- Implemented SQLite database loading
- Automatic table creation
- Persistent data storage

### 2. Monitoring & Logging (DevOps Requirement)
- File-based logging using pipeline.log
- Timestamped logs for each ETL stage
- Error tracking and debugging support

### 3. CI/CD Improvements
- Fixed module import errors in CI
- Updated Python version in pipeline
- Added pipeline log artifact upload
- Stable green CI pipeline achieved

### 4. Enhanced Testing
- Added database loading tests
- Improved reliability of test suite
- Full integration with CI pipeline

---

## Monitoring Implementation
The pipeline logs the following stages:
- Data Extraction
- Data Transformation
- Data Loading
- Errors and execution timestamps

Log file: `pipeline.log`

---

## Demonstration of Improved Increment
The system now:
- Executes full ETL (Extract, Transform, Load)
- Stores cleaned data in SQLite database
- Generates pipeline.log for monitoring
- Uploads logs as CI artifacts
- Runs successfully in GitHub Actions

Evidence:
- Green CI pipeline run
- Log file output (pipeline.log)
- SQLite database file generated
- Updated commit history showing Sprint 2 improvements

---

## Final Retrospective

### What Went Well
- Agile sprint structure improved project organization
- CI/CD pipeline enabled continuous testing
- Logging improved observability and debugging
- Incremental commits supported delivery discipline

### Challenges Faced
- Module import errors in CI environment
- Python version mismatch in GitHub Actions
- Initial pytest path configuration issues

### Key Improvements from Sprint 1 to Sprint 2
- Expanded pipeline from partial ETL to full ETL lifecycle
- Implemented monitoring and logging
- Resolved CI/CD failures and stabilized pipeline
- Increased automation and testing integration

### Key Lessons Learned
1. Agile iterative development improves software quality.
2. DevOps practices such as CI/CD and automated testing increase system reliability.
3. Proper project structure is critical for CI pipeline success.
4. Logging and monitoring are essential for production-ready data pipelines.

---

## Final System Architecture (Mermaid)
```mermaid
flowchart LR
    A[Raw Flight Dataset] --> B[Extract Module]
    B --> C[Transform Module]
    C --> D[Cleaned Dataset]
    C --> E[SQLite Database]
    B --> F[Logging System]
    F --> G[pipeline.log]
    B --> H[CI/CD Pipeline]
    H --> I[Automated Tests]
    H --> J[Artifact Upload - Logs]