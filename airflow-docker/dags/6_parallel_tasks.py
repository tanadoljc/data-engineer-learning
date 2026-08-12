from airflow.sdk import dag, task

@dag(
    dag_id="parallel_dag",
)
def parallel_dag():

    @task.python
    def fetch_data(**kwargs):
        # this is Task Instance
        ti = kwargs['ti']

        print("Extracting data ... this is the first task")
        extracted_data_dict = {'api_extracted_data':[1,2,3], 
                        'db_extracted_data':[4,5,6], 
                        's3_extracted_data':[7,8,9]}
        ti.xcom_push(key='return_res', value=extracted_data_dict)

    @task.python
    def transform_api_data(**kwargs):
        # this is Task Instance
        ti = kwargs['ti']
        fetched_data = ti.xcom_pull(task_ids='fetch_data', key='return_res')['api_extracted_data']
        transformed_api_data = [data*10 for data in fetched_data]
        ti.xcom_push(key='return_res', value=transformed_api_data)

    @task.python
    def transform_db_data(**kwargs):
        # this is Task Instance
        ti = kwargs['ti']
        fetched_data = ti.xcom_pull(task_ids='fetch_data', key='return_res')['db_extracted_data']
        transformed_db_data = [data*100 for data in fetched_data]
        ti.xcom_push(key='return_res', value=transformed_db_data)

    @task.python
    def transform_s3_data(**kwargs):
        # this is Task Instance
        ti = kwargs['ti']
        fetched_data = ti.xcom_pull(task_ids='fetch_data', key='return_res')['s3_extracted_data']
        transformed_s3_data = [data*1000 for data in fetched_data]
        ti.xcom_push(key='return_res', value=transformed_s3_data)

    @task.python
    def load_data(**kwargs):
        # this is Task Instance
        ti = kwargs['ti']
        
        api_data = ti.xcom_pull(task_ids='transform_api_data', key='return_res')
        db_data = ti.xcom_pull(task_ids='transform_db_data', key='return_res')
        s3_data = ti.xcom_pull(task_ids='transform_s3_data', key='return_res')

        return f"echo 'Loaded data: {api_data}, {db_data}, {s3_data}'"
    
    fetch_data = fetch_data()
    transform_api_data = transform_api_data()
    transform_db_data = transform_db_data()
    transform_s3_data = transform_s3_data()
    load_data = load_data()

    fetch_data >> [transform_api_data, transform_db_data, transform_s3_data] >> load_data

parallel_dag()