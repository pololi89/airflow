from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
from common.common_func import regist

with DAG(
    dag_id="dags_python_with_op_args",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    @task
    def regist_task(name, sex, *args):
        print(f'이름: {name}')
        print(f'성별: {sex}')
        print(f'기타옵션들: {args}')
    
    regist_t1 = regist_task('hjkim', 'man', 'kr', 'Seoul')
    
    # regist_t1 = PythonOperator(
    #     task_id = 'regist_t1',
    #     python_callable = regist,
    #     op_args = ['hjkim', 'man', 'kr', 'Seoul']
    # )
    
    # regist_t1