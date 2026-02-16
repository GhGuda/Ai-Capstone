import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform the dataset:
    - Remove duplicates
    - Handle missing values
    - Standardize column formats
    """
    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Standardize column names (lowercase)
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    return df
