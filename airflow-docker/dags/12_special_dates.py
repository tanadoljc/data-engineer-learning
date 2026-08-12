from airflow.sdk import dag, task
from datetime import datetime, timedelta
from airflow.timetables.events import EventsTimetable

special_dates = EventsTimetable(
    event_dates=[
        datetime(2026,1,1),
        datetime(2026,1,15),
        datetime(2026,1,26),
        datetime(2026,1,30),
    ]
)

@dag(
    schedule=special_dates,
    start_date=datetime(2026,1,1),
    end_date=datetime(2026,1,31),
    catchup=True,
)
def special_dates_dag():

    @task.python
    def special_event_task(**kwargs):
        execution_date = kwargs['logical_date']
        print(f"Executing special event task for date: {execution_date}")

    special_event = special_event_task()

special_dates_dag()