from airflow.sdk import dag, task

@dag(
    dag_id="xcoms_auto_dag"
)
def xcoms_auto_dag():

    @task.python
    def fetch_data():
        print("Extracting data ... this is the first task")
        fetched_data = {'data':[1,2,3,4,5]}
        return fetched_data

    @task.python
    def transform_data(data:dict):
        fetched_data = data['data']
        transform_data = {'transf_data':fetched_data * 2}
        return transform_data

    @task.python
    def load_data(data:dict):
        load_data = data
        return load_data

    fetch = fetch_data()
    transform = transform_data(fetch)
    load = load_data(transform)

    # We don't have to write this line
    # fetch >> transform >> load

xcoms_auto_dag()