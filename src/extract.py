import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extract data from CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        raise Exception("Dataset file not found.")
