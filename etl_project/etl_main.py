from extract import extract
from transform import transform
from load import load
from logger import get_logger

def etl():
    logger = get_logger()
    logger.info("ETL process started.")
    
    df = extract('source_data.csv')
    logger.info(f"Extracted {len(df)} rows.")
    
    df_transformed = transform(df)
    logger.info(f"Transformed data, now {len(df_transformed)} rows after filtering.")
    
    load(df_transformed)
    logger.info("Data loaded into SQL Server.")
    
    logger.info("ETL process completed.")

if __name__ == "__main__":
    etl()
