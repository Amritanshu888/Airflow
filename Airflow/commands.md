- To install Astro : winget install -e --id Astronomer.Astro
- astro dev init ---> Automatically it will initialize a astro project pulling the airflow development files from astro runtime 12.1.1
- It is going to initialize a empty astro project in this drive.
- astro dev init ---> It will initialize a project structure.

- In project structure we have dags folder --> which is basically for airflow.
- In project structure a Dockerfile is also created , once we run the entire project this will be the docker file which will run inside a docker container. --> This innternally also calls airflow and it will be running in one another port itself.
- Inside the dags folder only we basically create all our dags ---> an example file will already be there with name exampledag.py
- exampledag.py is a default example given by astro. Its a ETL example. Its getting astronaut details from the API , after getting info its returning the list of people in the space , then another task which is printing all the names. 2 specific tasks have been scheduled , when the api has new data we should be able to schedule it regularly.

## Run
- To run the project see in docker nothing should be running , docker should be installed and opened.
- command : astro dev start

- It will start building from here , its building the docker file , its building the docker image , its going to run each and everything in the docker itself.
- Now when u go to docker desktop u will see that ur containers have got started.
- If the Airflow UI doesn't gets opened automatically , u can go to docker and from there u can access web server.
- This is the Airflow UI , completely managed by Astro and this entirely is running in a docker container.
- In Airflow UI u will be able to see ur Dags getting created , right now there will be only one DAG i.e. example_astronauts , initially it will be disabled bocz u have not enabled.
- Go inside the DAG by double clicking it , there u will be able to see in this DAG i have two important tasks , 1. get_astronauts 2. print_astronaut_craft. When u double-click(also enable it) and get into it u will be able to see multiple things from the UI itself : Graph format, Gannt chart , code , run duration , task duration , calender ,event log ,details.
- In the UI u can see schedule which is set to daily , u also have the option to trigger this dag (available in UI basically ).
- Trigger is basically to run the DAG.
- Next run id will be there : Time at which it has to run next.
- Latest runid will be there : Time at which it ran previously.
- U can trigger it manually by clicking on the Trigger button. ---> Now both the tasks will be running.
- Go to graph after u press trigger , if the graph(both tasks in graph) is giving green signal then its basically running.
- After running go to get_astronauts in the DAG , in that u go to Event log u will be able to see previous logs , in code u can see Code.
- Logs will be basically for entire DAG. Code also u will be able to see.
- In example_astronauts there will be something called as Event/Audit log . All previous logs will be there.
- In UI we will also have something called as XCom ----> Which is basically what information is being passed from one task to the other task.

## Stop this:
- command : astro dev stop -----> after this my entire docker container will get stopped.
- Hence my entire application will also get stopped.

- In the project folder inside tests folder u have to write test cases.(By default for the exampledag.py test cases has been written).

- .env ---> if u want to write environment variables.
- airflow_settings.yaml ---> if u want to write settings over there.
- requirements.txt ----> if u want to install any libraries.
- README.md ---> To see the written info.
- All this is present in the project structure.

## Note:
- We create futher dags(tasks in that dag) in the dag folder only.

## Task API
- Airflow has a feature which is called as Task Flow API , which actually simplifies ur entire task creation process inside ur DAG , along with that u don't even have to go and create context , which we created with the help of xcom.
