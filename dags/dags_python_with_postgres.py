from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator

with DAG(
    dag_id='dags_python_with_postgres',
    start_date=pendulum.datetime(2025,4,1,tz='Asia/Seoul'),
    schedule=None,
    catchup=False
) as dag:
    
    def insrt_postgres(ip, port, dbname, user, passwrd, **kwargs):
        import psycopg2
        from contextlib import closing
        
        with closing(psycopg2.connect(host=ip, dbname=dbname, user=user, password=passwrd, port=int(port))) as conn:
            with closing(conn.cursur()) as cursur:
                dag_id = kwargs.get('ti').dag_id
                task_id = kwargs.get('ti').task_id
                run_id = kwargs.get('ti').run_id
                msg = 'insrt 수행'
                sql = 'insert into py_opr_drct_insrt_values (%s,%s,%s,%s);'
                cursur.execute(sql,(dag_id,task_id,run_id,msg))
                conn.commit()
                
    insrt_postgres = PythonOperator(
        task_id='insrt_postgres',
        python_callable=insrt_postgres,
        op_args=['172.28.0.3','5432','jbcha','jbcha','jbcha']
    )
    
    insrt_postgres