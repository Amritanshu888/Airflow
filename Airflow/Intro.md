## Apache Airflow
- Apache Airflow is an open-source platform used to programmatically author , schedule and monitor workflows. It allows you to define complex workflows as code and manage their execution . Airflow is commonly used for data pipelines , where tasks like data extraction , transformation , and loading (ETL) are orchestrated across multiple systems.

- Data Pipeline is created using ETL process -> Extraction , Transformation and Loading
- Extraction : From which source u have to extract(whether its API , Database).
- Transformation : Writing code for cleaning , processing or anything u want to do to the data.
- Loading : Loading in some data source(MongoDB , or some databases).
- Big data engineering team specifically creates this data pipeline/ETL pipeline. Once the ETL pipeline is created our data will be available in some source. This source can be any database , it can be MongoDB , MySql , Postgress. ---> data source depends on problem statement , it can also be stored in Amazon S3 bucket , json file format or some relational database.
- Once the data engineering team makes sure that our data is available in the data source , then the life cycle of the entire data science project goes on : 
- 1. Data Ingestion(we read the data from the data source) 
- 2. Feature Engineering(EDA,Handling Missing Values,Handling Outliers,Categorical Encoding,Normalization and Standardization) 
- 3. Feature Selection(Correlation,Forward Elimination,Backward Elimination , Univariate Selection, Random Forest Importance,Feature Selection with Decision Trees) 
- 4. Model Creation & Hyper parameter Tuning(GridSearchCV , RandomizedSearchCV , Keras Tuner , Bayesian Optimization - Hyperopt, Genetics Algorithm , Optuna)
- 5. Model Deployment(In cloud - Azure , AWS , GCP , HEROKU)
- 6. Model Monitoring & Retraining

## Note :
- Data keeps changing , hence our model should also be re-trained along with that changing data. This is what we do in 6th step above.

- ETL pipeline continiously works along with changing data.

- When we take this entire project into the production , then model monitoring , model retraining , getting the new data , needs to be automated completely ---> as we cannot do each and every manual task.
- This entire process needs to be automated. Automate the ETL process. Every day , every night i should be getting a new data in my datasource.
- In the life cycle of a data science project whenever the model accuracy decreases , i should automate this retraining process , it may happen every bi weekly , once in a week --> that process needs to be completely automated and that is where this Airflow(Open Source platform) will be used.
- To automate this entire process we can specifically use airflow.

- To automate this ETL pipeline and the entire data science project lifecycle we can use Apache Airflow over here.

- The automation will happen in such a way that this we can schedule(this process can be entirely scheduled) --> with the help of airflow , like how frequently u want the model to be trained , how frequently u want the ETL pipeline updating ur entire datasource.

- The multiple steps in life cycle of a data science project(feature engineering , feature selection , and further) this all can be considered as a task in airflow.
- When we consider this as a task in airflow , so we can create all the task and we can create in such a way that we can also make ensure that in which step or process these tasks need to be executed. ---> all with the help of airflow.

- Here u can also see logs , u can also see how this entire flow is going on , u can create entire modules in the form of graph and then u can probably monitor it.

## Key Concepts in Apache Airflow
## (Key components in Airflow)
- 1. DAG (Directed Acyclic Graph) ---> Directed Graph(We are giving some direction for this particular graph)
- DAG is a collection of tasks that u want to schedule and run. In lifecycle of a data science project , data ingestion , feature engineering , feature selection and further , these all are independent modules and we can consider these all as specific tasks.
- Let's say i have multiple tasks , like task A , task B , task C , in this scenario a directed acyclic graph will be a combination/collection of tasks.
- In DAG we have tasks in a directed way. That is there is a flow in which tasks need to be executed. Task A --> Task B --> Task C.
- Each DAG is a directed graph meaning that the flow of tasks has a direction from one task to the another task and it is acyclic.
- 2 Core Properties : 1.Directed 2.Acyclic
- Directed : Tasks must have a specific sequence.
- Acyclic : As the name says it means that no task should depend on itself.
- Nodes represent a task , edges represent a direction. Direction can also be reverse , A >>> B >>> C , first A got executed , then B and then C. In reverse : A <<< B <<< C.

- 2. Tasks
- Task represent the individual unit of work in a DAG. Like in life cycle of a data science project data ingestion , feature engineering , feature selection these all are seperate one task.
- In Airflow task can be anything : Python function , querying a database , sending an HTTP request , it can be any type of task.

- 3. Dependencies
- Tasks in a DAG have dependencies , meaning one task might need to finish before another task can start. These dependencies allow u to control the order in which tasks are executed. Airflow provides mechanisms like set_upstream and set_downstream to define these dependencies between tasks.

## Why Airflow for MLOPS ??
- In MLOps (Machine Learning Operations), orchestrating ML workflows effeciently is crucial for ensuring that data pipelines , model training , and deployement tasks happen smoothly and in an automated manner. Airflow is well-suited for this purpose because it allows you to define , automate , and monitor every step in a ML pipeline.

## Reasons why Airflow is a fit for MLOPS
- 1. Orchestrating ML Pipelines and ETL Pipelines
- In lifecycle of a data science project : Data Ingestion---->Data Preprocessing------>Model Training and Eval--->Model Deployment (Basic 4 fundamental modules).
- Orchestrating a ML/ETL pipeline meaning : To automate the above tasks in lifecycle of a data science project airflow is a amazing tool.
- At the end of the day with the help of airflow we create DAG(Directed Acyclic Graph).
- In DAG u will be able to define the tasks , and u will be able to define dependencies.(Task and Dependencies: What order every step is going to execute).
- Once we deploy this entire application into the production , all the steps need to be executed in a automated way.(No manual tasks envolved over here). Hence here airflow is useful.

- 2. Task Automation

- 3. Monitoring and Alerts
- By using Airflow u can schedule each and every thing. U can schedule ETL pipeline like how frequently i want my data to be captured in my source. Let's say weekly.
- How frequently i want to do my model retraining.
- How regularly u want to execute the entire data science project lifecycle.
- It provides real time monitoring (Airflow has Airflow UI), u will be able to see the logs.
- We will be able to see the task logs(Crucial to know how things are getting executed).
- Alerts and Notifications(Eg. Mail, Mail alterts , slack alerts).

- 4. Retry Mechanisms
- Let's say we want to implement data ingestion for which i m reading from an API and then suddenly there is a network failure during a data fetch ------> so in Airflow their is a concept called as Retry Mechanisms ----> it will try that specific tasks based on some rule.
It will retry the task based on some predefined rule.

## Astronomer
- An application which will be running Airflow inside a Docker Container.

- In our projects we will be using multiple services , which will be running inside our docker container , later we will make ensure that using docker compose we will make them interact altogether.
- Astro is managed platform for running the entire Apache Airflow , where everything is basically running in a docker container.
