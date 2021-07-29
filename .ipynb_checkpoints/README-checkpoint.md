![ETL Workflow](https://github.com/pinocchioVirus/data-analysis-workflow/actions/workflows/etl-proccess.yml/badge.svg)
![SonarCloud Scan](https://github.com/pinocchioVirus/data-analysis-workflow/actions/workflows/sonar-cloud.yml/badge.svg)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=pinocchioVirus_sideProject&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=pinocchioVirus_sideProject)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=pinocchioVirus_sideProject&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=pinocchioVirus_sideProject)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=pinocchioVirus_sideProject&metric=security_rating)](https://sonarcloud.io/dashboard?id=pinocchioVirus_sideProject)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=pinocchioVirus_sideProject&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=pinocchioVirus_sideProject)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=pinocchioVirus_sideProject&metric=code_smells)](https://sonarcloud.io/dashboard?id=pinocchioVirus_sideProject)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=pinocchioVirus_sideProject&metric=bugs)](https://sonarcloud.io/dashboard?id=pinocchioVirus_sideProject)

# Dashboard using CI/CD, Automation, Docker and SonarCloud
Project focuss on automating and containerizing the proccess of data <b>ETL (extract, transform, load)</b> and importing into our chosen database, to build a dashboard and analyzing it using <b>Superset</b> with our <b>Automated Data</b>.

### Topics:
- <a href="#automating-etl-process">Data Automation Process</a>
- <a href="#cicd-workflow-process">CI/CD Workflow Process</a>
- <a href="#containerization-process">Containerization Workflow Process</a>

### Used in this project:
- <a href="https://ubuntu.com/">Ubuntu</a> 20.04 LTS (OS) on local and inside containers
- <a href="https://sqlite.org/index.html">SQLlite3</a> (Storage)
- <a href="https://www.postgresql.org/">PostgreSQL</a> on Heroku (Backup)
- <a href="https://superset.apache.org/">Superset</a> (Dashboards and Reports)
- <a href="https://pypi.org/project/jupyterlab/">JupyterLab</a> (Data Analysis and Engineering)
- <a href="https://github.com/features/actions">Github Actions</a> (CI/CD)
- <a href="https://sonarcloud.io/">SonarCloud</a> (Code Quality and Code Security) 
- <a href="https://www.python.org/downloads/">Python 3.8+</a> (Programming language)
- <a href="https://www.sublimetext.com/">Sublime Text</a> (Code Editor) 
- Containerization (Docker, Docker Compose)
   - <a href="https://hub.docker.com/_/ubuntu">Ubunut 20.04 LTS</a> (OS)
   - <a href="https://hub.docker.com/_/postgres">PostgreSQL</a> (DB), <a href="https://hub.docker.com/r/dpage/pgadmin4">pgADmin</a> (DBA)

# Automating ETL Process
#### You can run the project by running the following commands (Inside 'code/' Folder), after reading the requirements here:
Before you run the code, make sure to set your sql instance configurations if you want to connect to other DB service provider or LocalDB (Like PostgreSQL/MySQL/MSSQL) in the following file:
```python
code/configurations/SQL_Config.py
``` 
Then after adding your configurations (Or if you want to use SQLite3 as your storge db edit/add on the 'transferData.py file') and downloaded needed packages (can found in 'requirements.txt'), excute the code script to import data into the database.

To run the 'ETL' process, make sure to run the following command to install and save the data to the dataset folder, and make sure you are in the right path (code/):
```python
python3 code/etl_data.py
```

We have the dataset and we are ready now to import the data into our database, by running the following command:
```python
python3 code/transfer_data.py
```

Finally, you can automate above process by running a shell script to automatically run both files and also create .sql file in case you have another database to import into it, without needing to take the same proccess to insert data and you just have to import into the database the generated .sql file (make sure you make the shell file excutable by running: 'chmod +x esc.sh') by running the following command:
```python
./esc.sh
```

# CI/CD Workflow Process
We automated the process of <b>'ETL'</b> using shell script and it works right? but, we have still need to run it manualy inside <b>'terminal'</b> and this makes half of the process are not automated, and here where comes the subject of <b>'CI/CD'</b> and we can create custom <b>'continuous integration (CI)'</b> and <b>'continuous deployment (CD)'</b> workflows directly inside our GitHub repository with <a href="https://github.com/features/actions"><b>GitHub Actions</b></a>.

### Steps To Use CI/CD:
- Go to repository > actions > setup python
- Then copy './github/workflows/etl-proccess.yml' inside your created file
   - Note: make sure you configure as you prefer it to work 
- If you want sonarcloud to be your code quality/security chosen tool:
   - create 'sonar-project.properties' file and put your configurations on it
   - copy './github/workflows/sonar-cloud.yml' inside your created file
   - Note: make sure you configure as you prefer it to work
 
After you configured and enabled github actions, your 'ETL' process now is compatible with 'CI/CD' and the dataset is scheduled to be automaticly downloaded and transfered to the databasefor every 40min <b>'ksa/riyadh'</b> time and after it completed 5min later sonarcloud scan runs and checks the code security and code quality.

# Containerization Process
If you wanna to use containers as your lab, test or even for developing analysis solution (like in example predicting next week rates and cases based on the data you have automated), you can use docker containers to run isolated environment for you to work on.

In this project i have used Dockerfile (found it on the root folder) to configure the installation of jupyter-lab and python3 with requirements packages (also found it on the root folder), and used docker-compose to install and configure multiple-containers (3 isolated containers with different purposes) to handle our backup database (PostgreSQL), Adminstration Console (pgAdmin) and NoteBook (Jupyter-lab).

#### In case you need to Containerize your ETL & Analysis Infrastructure with Docker as an isolated environment for analysis or testing etc., make sure you have first installed <a href="https://docs.docker.com/get-docker/"><b>Docker</b></a> and you have also <a href="https://docs.docker.com/compose/install/"><b>Docker Compose</b></a>. Now you are ready to use the project by following next easy steps:

#### I put two files in the root folder for containerizing the project called "Dockerfile" and  "docker-compose.yml". <b>Dockerfile</b> is handling the process of installing ubuntu image and installs inside the image all jupyterlab prerequisite packages along with all its confirgurations, <b>docker-composer.yml</b> is used to download multi-container applications using <a href="https://hub.docker.com/">DockerHub</a> images and making the process of installing multi-containers with its configuration more easy!.

After we have maked sure that docker and docker-compose are installed on our machine also up and running, for testing purpose on isolated environment with docker container you can simply run the following command (Inside root directory):
```python
docker build -t testing .
```
And you can see if the container is created or not:
```python
docker ps
```
Then, after we have installed our container successfully run the following command to make it run inside isolated environment on docker:
```python
docker run -d -p 8888 testing
```
We have successfully running isolated jupyterlab environment on docker, and can access it using your browser and go to the following path:
```python
localhost:8888
```

#### After we saw how we can isolate our workflow for mare easy way to work without needing to take care of the environment each and single time, but also there is another way for installing multi-container which is what we need ex: (PostgreSQL, PgAdmin and JupyterLab all together) in this case we gonna use <b>docker-compose</b>, just by running following command:
```python
docker-compose up -d
```
And we gonna see that a new proccess is running and installing all needed images and configurations as we typed on the docker-compose.yml file, and we can see afer the install process finish all three container are up and running just run the following command now:
```python
docker-compose ps
```

# Link To The Dashboard:
<table class="tg">
  <tr>
    <th class="tg-yw4l"><b>Name</b></th>
    <th class="tg-yw4l"><b>Description</b></th>
    <th class="tg-yw4l"><b>Link</b></th>
  </tr>
  <!-- Dashboard Links -->
  <tr>
    <td class="tg-yw4l">Covid Dashboard</td>
    <td class="tg-yw4l">Dashboard of Saudi Arabia Cases and vaccinations rates in real-time</td>
    <td class="tg-yw4l"><a href="#">
      <p>Soon</p>
    </a></td>
  </tr>
</table>
