from first_orchestrator_dag import first_orchestrator_dag
from second_orchestrator_dag import second_orchestrator_dag
from airflow.sdk import dag, task
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

@dag
def parent_orchestrator_dag():

    trigger_first_dag = TriggerDagRunOperator(
        task_id="trigger_first_dag",
        trigger_dag_id="first_orchestrator_dag",
        wait_for_completion=True,
        poke_interval=10,
        allowed_states=["success", "failed"]
    )

    trigger_second_dag = TriggerDagRunOperator(
        task_id="trigger_second_dag",
        trigger_dag_id="second_orchestrator_dag",
        wait_for_completion=True,
        poke_interval=10,
        allowed_states=["success", "failed"]
    )

    trigger_first_dag >> trigger_second_dag

parent_orchestrator_dag()