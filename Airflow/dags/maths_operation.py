"""
We'll define a DAG where the tasks are as follows:

Task 1: Start with an initial number (e.g., 10).
Task 2: Add 5 to the number.
Task 3: Multiply the result by 2.
Task 4: Subtract 3 from the result.
Task 5: Compute the square of the result.

"""
## The above basic example is just for understanding how do we create a proper pipeline.

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

## Define function for each task
## In the below functions this context will be responsible for providing the information/output from a particular function to other function ,
## bcoz their is a dependency , first i have to execute this function then go ahead with other function.
def start_number(**context):
    ## We will set context value by using a very important function i.e. Xcom_push ---> Which is again provided by Airflow.
    ## This value we will save in that so that we can share those values within the tasks.
    context["ti"].xcom_push(key='current_value',value=10) ## Assigning the value as 10.
    ## What the above code is basically doing is that in this related context i m setting the value of the current_value to 10.
    print("Starting number 10") ## Whenever we print this it will be saved in the log information when we are running the entire DAG.

def add_five(**context):
    current_value = context["ti"].xcom_pull(key='current_value',task_ids='start_task') ## Passing the same key , i m defining some ids also over here.
    ## Note: When we are calling this we have to call this task id considering the previous task.
    ## When i m pulling this information , the recent value w.r.t the current value that i will get.
    new_value = current_value + 5  ## Here in this function the current value should be coming from the start function.
    context["ti"].xcom_push(key='current_value',value=new_value) ## Pushing the new value
    print(f"Add 5:{current_value}+5={new_value}")

def multiply_by_two(**context):
    current_value = context["ti"].xcom_pull(key='current_value',task_ids='add_five_task') ## We will get recent value of whatever the current value is assigned --> Which is our new_value.
    ## In task_ids we are giving the previous tasks info here
    new_value = current_value*2
    context["ti"].xcom_push(key='current_value',value=new_value) ## From this particular xcom_push() function i can convert key-value to json also.
    print(f"Multiply by 2: {current_value}*2 = {new_value}")

def subtract_three(**context):
    current_value = context["ti"].xcom_pull(key='current_value',task_ids='multiply_by_two_task') ## Task id given w.r.t previous task
    ## Task id is nothing but just an indication that whatever is the output of that particular function(previous function) that is being basically represented by this task id.
    new_value = current_value - 3
    context["ti"].xcom_push(key='current_value',value=new_value)
    print(f"Subtract 3:{current_value} - 3 = {new_value}")

def square_number(**context):
    current_value = context["ti"].xcom_pull(key='current_value',task_ids='subtract_three_task') ## This id u can name it anyhow nothing is fixed , but the best practice: make it represent the previous task.
    new_value = current_value ** 2
    print(f"Square the result: {current_value}^2 = {new_value}")

## Define the DAG
with DAG(
    dag_id = 'math_sequence_dag', ## Basically pipeline name
    start_date = datetime(2025,1,1),
    schedule = '@once', ## U have to run it once until and unless i trigger it , if i write weekly it will run per week.
    catchup = False
) as dag:
    ## Define the task
    ## The task ids mentioned above in the above functions should be mapped here in PythonOperator , so that this function will automatically understand what task id to use.
    start_task = PythonOperator(task_id='start_task',python_callable=start_number,provide_context=True) ## As we have already provided context we say provide_context = True
    ## When we say provide_context=True then this xcom will be responsible in providing context from one task to the other task.
    add_five_task = PythonOperator(task_id='add_five_task',python_callable=add_five,provide_context=True)
    multiply_by_two_task = PythonOperator(task_id='multiply_by_two_task',python_callable=multiply_by_two,provide_context=True)
    subtract_three_task = PythonOperator(task_id='subtract_three_task',python_callable=subtract_three,provide_context=True)
    square_number_task = PythonOperator(task_id='square_number_task',python_callable=square_number,provide_context=True)
    ## The reason why we are using a PythonOperator because we know that this is a python function.
    ## Based on context and task id we are able to pass the information from one task to the other task.

    ## Set the Dependencies
    start_task >> add_five_task >> multiply_by_two_task >> subtract_three_task >> square_number_task

## Command : astro dev start ---> Once u execute this ur entire docker container will start building again. (Docker container is getting started)
# Note : provide_context argument is no longer accepted now in Airflow its invalid.
## Note: All the print statement outputs in the above functions u will be able to see them in logs of each and every particular task in this DAG.
## Also for each task u will have Xcom --> This will contain the value exchanged between functions/tasks.
## In square number task no Xcom value as u did not pushed/saved anything , but in log print statement will be there.
## Everything will be working in different containers and those containers will be communicating with each other.



