from airflow import DAG
from airflow.sensors.filesystem import FileSensor
import pendulum

with DAG(
    dag_id='dags_file_sensor',
    start_date=pendulum.datetime(2025,4,1,tz='Asia/Seoul'),
    schedule='0 7 * * *',
    catchup=False
) as dag:
    TbCorona19CountStatus_sensor = FileSensor(
        task_id='TbCorona19CountStatus_sensor',
        fs_conn_id='conn_file_opt_airflow_files',
        filepath='TbCorona19CountStatus/{{execution_date.in_timezone("Asia/Seoul") | ds_nodash}}/TbCorona19CountStatus.csv',
        recursive=False,
        poke_interval=60,
        timeout=60*60*24,
        mode='reschedule'
    )