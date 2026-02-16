from src.extract import extract_data
from src.transform import clean_data
from src.load import load_to_database
import logging

# Configure logging
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    try:
        logging.info("===== ETL Pipeline Started =====")

        file_path = "raw_bangladesh_data/Flight_Price_Dataset_of_Bangladesh.csv"

        # Extract Stage
        logging.info("Starting data extraction...")
        raw_data = extract_data(file_path)
        logging.info(f"Data extraction completed. Rows loaded: {len(raw_data)}")

        # Transform Stage
        logging.info("Starting data transformation...")
        clean_df = clean_data(raw_data)
        logging.info(f"Data transformation completed. Rows after cleaning: {len(clean_df)}")

        # Save cleaned CSV
        output_csv = "raw_bangladesh_data/cleaned_flight_data.csv"
        clean_df.to_csv(output_csv, index=False)
        logging.info(f"Cleaned data saved to {output_csv}")

        # Load Stage (Sprint 2 improvement)
        logging.info("Loading data into SQLite database...")
        load_to_database(clean_df)
        logging.info("Database loading completed successfully")

        logging.info("===== ETL Pipeline Completed Successfully =====")

    except Exception as e:
        logging.error(f"Pipeline failed due to error: {str(e)}")
        print("Pipeline failed. Check pipeline.log for details.")

if __name__ == "__main__":
    run_pipeline()