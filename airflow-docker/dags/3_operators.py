from airflow.sdk import dag, task

@dag(
    dag_id="operators_dag"
)
def operators_dag():

    @task.python
    def first_task():
        print("This is first task")

    @task.python
    def second_task():
        print("This is second task")

    @task.python
    def third_task():
        print("This is third task")

    @task.bash
    def bash_task():
        return f"echo 'This is Bash Task'"

    first = first_task()
    second = second_task()
    third = third_task()
    bash = bash_task()

    first >> second >> third >> bash

operators_dag()