## ETL Pipelines
- There are 3 key terms:
- 1. Extract 
- 2. Transform
- 3. Load

- Big data engineering team goes and follows this ETL pipeline process. This ETL pipeline is the part of the data pipeline.
- Suppose we have a source from where we have to take data for our problem statement this source can be API's , Internal Database , IOT devices , similarily there can be various sources.
- What data engineering person will do ??
- We need to go ahead and create something called as data pipeline. In this data pipeline our main task is to integrate or combine all these data sources(sources mentioned above) together and then do some kind of preprocessing and transformation on them.
- In preprocessing and transformation what i can do as data scientist is that (we have combined all the data) then we convert it into a json format which will have the entire data together. So this part where we are basically taking data from the source is called as extract.
- When we are doing preprocessing and transformation its basically transform phase. Cleaning of the data and then convert it into a format (json) is basically Transform phase.
- Why converting to json ??
- All these combined data will be stored in one specific source , and when further going ahead the data scientists will be dependent on this source only. They will not be dependent on multiple sources available over here.
- We will take this json and store it in some kind of source.(This is loading phase as here we are loading the data in some source).
- Transformation we have done by converting it into json and then loading it in one particular source is the load phase.
- This source can be ur SQL server , MongoDB server , it can also be ur Postgres Server or NoSQL data (anything upto u).
- Then data scientists need to be only dependent on this one source as all this data is basically getting combined and then stored in one source.
- This is the reason we say this as ETL(Extract,Transform,Load). This ETL we say this as Data Pipeline bcoz its collecting data from various sources , combining them , and then loading them into a specific source.

- Airflow is a amazing open source platform which will actually help u to create this amazing data pipelines which includes this extract , transform , load.
- In projects we will take the data from an API (basically read the data from an API) ---> then transform it into json format ----> then will save this in some kind of database(the database we will use here is postgres SQL).
- We will run this database in docker container. ---> Will give us an idea that in airflow how can we communicate from one container to the other container.
- Why using Airflow ??
- Bcoz the process mentioned above in projects needs to be completely scheduled , bcoz for my problem statement i need to get data every week/day. Inorder to schedule in this way we have to use something called as Airflow.
- Airflow is basically helping us in scheduling our ETL pipeline.
- We will run everything in docker container as this will allow it to be independent while deploying.
