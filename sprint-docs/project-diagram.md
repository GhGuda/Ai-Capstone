```mermaid
flowchart LR
    A[New Flight_Price_Dataset_of_Bangladesh.csv] --> B[n8n Trigger]
    B --> C[Read CSV Schema]
    C --> D[Compare with Stored Schema JSON]
    D --> E{Schema Changed?}

    E -- No --> Z[Exit Workflow]

    E -- Yes --> F[Chat AI]
    F --> G[Structured JSON Output:
        - Updated transform logic
        - Required test changes
        - Risk summary]

    G --> H[n8n Parses JSON]
    H --> I[Create Git Branch]
    I --> J[Send Structured Prompt to IDE AI]
    J --> K[Update transform.py]
    K --> L[Regenerate test_pipeline.py]
    L --> M[Commit & Push]

    M --> N[GitHub Actions CI/CD]
    N --> O{Tests Pass?}

    O -- No --> P[Send pipeline.log to Chat AI]
    P --> Q[Root Cause Analysis + Patch]
    Q --> J

    O -- Yes --> R[Merge PR + Notify]
