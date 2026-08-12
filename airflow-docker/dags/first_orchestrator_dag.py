from airflow.sdk import dag, task
import os

@dag(
    dag_id="first_orchestrator_dag"
)
def first_orchestrator_dag():

    @task.python
    def first_task():
        print("This is first task")

    @task.python
    def second_task():
        print("This is second task")

    @task.python
    def third_task():
        os.makedirs(os.path.dirname("/opt/airflow/logs/data/orchestrated_1_data.txt"), exist_ok=True)

        with open("/opt/airflow/logs/data/orchestrated_1_data.txt", 'w') as f:
            f.write(f"Data processed successfully\n")

        print(f"Data processing completed and saved to /opt/airflow/logs/data/orchestrated_1_data.txt")

    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third

first_orchestrator_dag()