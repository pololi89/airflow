from airflow import DAG
import datetime
import pendulum
from airflow.providers.http.operators.http import HttpOperator
from airflow.decorators import task

with DAG(
    dag_id="dags_http_opeartor",
    schedule=None,
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    """서울시 공공자전거 대여소 정보"""
    tb_cycle_station_info = HttpOperator(
        task_id='tb_cycle_station_info',
        http_conn_id='openapi.seoul.go.kr',
        endpoint='{{var.value.apikey_openapi_seoul_go_kr}}/json/tbCycleStationInfo/1/10/',
        method='GET',
        headers={'Content-Type': 'application/json',
                        'charset': 'utf-8',
                        'Accept': '*/*'
                 }
    )
    
    @task(task_id='python_2')
    def python_2(**kwargs):
        ti = kwargs['it']
        rslt = ti.xcom_pull(task_id='tb_cycle_station_info')
        import json
        from pprint import pprint
        
        pprint(json.loads(rslt))
        
    tb_cycle_station_info >> python_2()