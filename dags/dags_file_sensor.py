from airflow import DAG
from airflow.sensors.filesystem import FileSensor
import pendulum

with DAG(
    dag_id='dags_file_sensor',
    start_date=pendulum.datetime(2025,4,1,tz='Asia/Seoul'),
    schedule='0 7 * * *',
    chatchup=False
) as dag:
    tvCorona19VaccineStatNew_sensor = FileSensor(
        task_id='tvCorona19VaccineStatNew_sensor',
        fs_conn_id='conn_file_opt_airflow_files',
        filepath='tvCorona19VaccinestatNew/{{execution_date.in_timezone("Asia/Seoul") | ds_nodash}}/tvCorona19VaccinestatNew.csv',
        recursive=False,
        poke_interval=60,
        timeout=60*60*24,
        mode='reschedule'
    )