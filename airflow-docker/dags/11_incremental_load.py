from airflow.sdk import dag, task
from datetime import datetime, timedelta
from airflow.timetables.interval import CronDataIntervalTimetable

@dag(
    dag_id="incremental_load_dag",
    schedule=CronDataIntervalTimetable('@daily',timezone='UTC'),
    start_date=datetime(2026, 8, 1),
    end_date=datetime(2026, 8, 4),
    catchup=True,
)
def incremental_load_dag():
    
    @task.python
    def incremental_data_fetch(**kwargs):
        date_interval_start = kwargs['data_interval_start']
        date_interval_end = kwargs['data_interval_end']
        print(f"Fetching incremental data from {date_interval_start} to {date_interval_end}")

    @task.bash
    def incremental_data_process():
        return "echo 'Processing incremental data {{data_interval_start}} to {{data_interval_end}}'"
    
    fetch_task = incremental_data_fetch()
    process_task = incremental_data_process()

    fetch_task >> process_task

incremental_load_dag()