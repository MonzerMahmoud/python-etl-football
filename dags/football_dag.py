from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import sys
sys.path.append('/Users/syberexpertise/Desktop/CODING/python-football-ETL')
from football_etl import run_football_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(0,0,0,0),
    'email': ['monzer@test.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'football_dag',
    default_args=default_args,
    description='Extract football data from football-data.org',
    schedule_interval=timedelta(seconds=30)
)

def just_print_world():
    print("Hello World")

run_etl = PythonOperator(
    task_id='run_etl',
    python_callable=run_football_etl,
    dag=dag
)

run_etl