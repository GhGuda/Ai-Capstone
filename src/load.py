import sqlite3
import pandas as pd

def load_to_database(df: pd.DataFrame, db_name="flight_data.db"):
    """
    Load cleaned data into SQLite database.
    """
    conn = sqlite3.connect(db_name)
    df.to_sql("cleaned_flights", conn, if_exists="replace", index=False)
    conn.close()
