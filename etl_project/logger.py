import logging

def get_logger():
    logger = logging.getLogger("ETL_Logger")
    logger.setLevel(logging.INFO)
    
    fh = logging.FileHandler("etl_log.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    return logger
