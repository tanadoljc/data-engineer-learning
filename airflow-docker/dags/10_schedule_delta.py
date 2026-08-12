from airflow.sdk import dag, task
from datetime import datetime, timedelta

@dag(
    dag_id="schedule_cron_dag",
    start_date=datetime(2026, 8, 8),
    schedule=timedelta(days=1),
    end_date=datetime(2026, 8, 31),
    is_paused_upon_creation=False,
    catchup=True,
)
def schedule_cron_dag():

    @task.python
    def first_task():
        print("This is first task")

    @task.python
    def second_task():
        print("This is second task")

    @task.python
    def third_task():
        print("This is third task")

    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third

schedule_cron_dag()