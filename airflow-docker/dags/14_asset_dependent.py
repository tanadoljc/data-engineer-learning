from datetime import datetime
from airflow.sdk import dag, task, asset
import os
from 13_assets import fetch_data

@asset(
    schedule=fetch_data,
    uri="/opt/airflow/logs/data/data_processed.txt",
    name='process_data'
)
def process_data(self):

    os.makedirs(os.path.dirname(self.uri), exist_ok=True)

    with open(self.uri, 'w') as f:
        f.write(f"Data processed on {datetime.now()}\n")

    print(f"Data processing completed and saved to {self.uri}")