from airflow import DAG
from airflow.operators.python import PythonOperator ## It is just used to define a task(responsible for executing python functions in the tasks)
from datetime import datetime

## Define our task 1 ---> When we are creating DAG , inside DAG we need to have tasks(which will be having dependencies)----->
## We will follow a specific flow which tasks need to be executed first and in what direction it really needs to be executed.
## We will execute all the tasks in a specific order in a directed graph.
def preprocess_data():
    print("Preprocessing data....")

## Define our task 2
def train_model():
    print("Training model...")

## Define our task 3
def evaluate_model():
    print("Evaluate Models...")

## Define the DAG
with DAG(
    'ml_pipeline', ## First parameter is our DAG name
    start_date = datetime(2025,1,1), ## From which date u want to start
    schedule = '@weekly' ## Here we have multiple options like daily , weekly etc. its abt how u want to execute this pipeline , like how frequently.
    ## Writing weekly means we want to execute this weekly.
) as dag:
    ## Here we are inside this DAG block
    ## Define the task(using variables while defining, we have to execute the functions which we have defined above , preprocess is a variable here)
    preprocess  = PythonOperator(task_id="preprocess_task",python_callable=preprocess_data) ## function which we have to call is passed in python_callable
    train = PythonOperator(task_id="train_task",python_callable=train_model)
    evaluate = PythonOperator(task_id="evaluate_task",python_callable=evaluate_model)

    ## Set Dependencies(Order in which u have to execute)
    preprocess >> train >> evaluate ## This is how we specify the order of execution

## Start the execution by using command : astro dev start    
## After this it will be available in DAG in Airflow UI , u will be able to see 3 different tasks when u go in this DAG.
## Trigger it manually , all tasks will be in green , select preprocess_task , u will be able to see its logs.
## In Airflow UI u will be able to see all my dags , tasks in them , logs , also see Xcom(responsible for holding info passed from one task to the other task).
## Stop it : astro dev stop

## Now let us suppose ur container is already running and i want to change some code and then i want to run this so for this:
## Use command : astro dev restart ----> Automatically ur entire container will get restarted.