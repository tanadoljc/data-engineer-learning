from airflow.sdk import dag, task

@dag(
    dag_id="xcoms_kwargs_dag"
)
def xcoms_kwargs_dag():

    @task.python
    def fetch_data(**kwargs):
        # this is Task Instance
        ti = kwargs['ti']

        print("Extracting data ... this is the first task")
        fetched_data = {'data':[1,2,3,4,5]}
        ti.xcom_push(key='return_res', value=fetched_data)

    @task.python
    def transform_data(**kwargs):
        # this is Task Instance
        ti = kwargs['ti']

        fetched_data = ti.xcom_pull(task_ids='fetch_data', key='return_res')['data']
        transformed_data = {'transf_data': fetched_data * 2}
        ti.xcom_push(key='return_res', value=transformed_data)

    @task.python
    def load_data(**kwargs):
        # this is Task Instance
        ti = kwargs['ti']
        
        loaded_data = ti.xcom_pull(task_ids='transform_data', key='return_res')['transf_data']
        return loaded_data

    fetch = fetch_data()
    transform = transform_data()
    load = load_data()

    fetch >> transform >> load

xcoms_kwargs_dag()