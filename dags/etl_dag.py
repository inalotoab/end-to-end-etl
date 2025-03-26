from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Add your project path so Airflow can find your modules
sys.path.append(os.path.abspath("/opt/airflow/etl_project"))

from extract import extract
from transform import transform
from load import load

csv_path = '/opt/airflow/etl_project/data/source_data.csv'

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='split_etl_pipeline',
    default_args=default_args,
    description='Split ETL: Extract, Transform, Load separately',
    schedule_interval='@weekly',
    start_date=datetime(2025, 3, 25),
    catchup=False,
    tags=['etl', 'split', 'sqlserver'],
) as dag:

    def extract_wrapper(**kwargs):
        df = extract(csv_path)
        df.to_pickle('/tmp/extracted.pkl')

    def transform_wrapper(**kwargs):
        import pandas as pd
        df = pd.read_pickle('/tmp/extracted.pkl')
        df = transform(df)
        df.to_pickle('/tmp/transformed.pkl')

    def load_wrapper(**kwargs):
        import pandas as pd
        df = pd.read_pickle('/tmp/transformed.pkl')
        load(df)

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract_wrapper
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform_wrapper
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load_wrapper
    )

    extract_task >> transform_task >> load_task
    
    # Add this at the bottom of etl_dag.py
dag = dag


