from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator_with_template",
    schedule="10 0 L * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    # START_DATE: 전월 말일, END_DATE: 1일 전
    bash_task_1 = BashOperator(
        task_id='bash_task_1',
        env={'START_DATE':'{{ }}',
             'END_DATE':'{{}}'
        },
        bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
    )