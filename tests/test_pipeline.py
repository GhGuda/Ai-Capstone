import sys
import os

# Add project root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from src.extract import extract_data
from src.transform import clean_data
from src.load import load_to_database


def test_extract_data():
    df = extract_data("raw_bangladesh_data/Flight_Price_Dataset_of_Bangladesh.csv")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_clean_data():
    sample_data = {
        "Airline": ["A", "A", None],
        "Price": [100, 100, 200]
    }
    df = pd.DataFrame(sample_data)

    cleaned_df = clean_data(df)

    # No null values after cleaning
    assert cleaned_df.isnull().sum().sum() == 0


def test_database_loading():
    df = pd.DataFrame({
        "airline": ["TestAir"],
        "price": [100]
    })

    load_to_database(df, "test.db")
    assert os.path.exists("test.db")
