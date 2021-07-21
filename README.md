[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=pinocchioVirus_sideProject&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=pinocchioVirus_sideProject)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=pinocchioVirus_sideProject&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=pinocchioVirus_sideProject)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=pinocchioVirus_sideProject&metric=code_smells)](https://sonarcloud.io/dashboard?id=pinocchioVirus_sideProject)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=pinocchioVirus_sideProject&metric=bugs)](https://sonarcloud.io/dashboard?id=pinocchioVirus_sideProject)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=pinocchioVirus_sideProject&metric=security_rating)](https://sonarcloud.io/dashboard?id=pinocchioVirus_sideProject)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=pinocchioVirus_sideProject&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=pinocchioVirus_sideProject)


# Covid-19 Dashboard using CI/CD Methodology
Self Challenge To Build Dashboard for Covid-19 and Analyzing it using Google Data Studio.
### Tech Used in This Challenge:
- Databases (SQLlite3, PostgreSQL)
   - Storge, Backuup
- Google Data Studio (Dashboard) and Jupyter Notebook (Analysis)
- Github Actions (CI/CD) and SonarCloud (Code Quality and Code Security) 
- Python 3.8+ (Language)
   - All Packages Used are Found In : requirements.txt
- Sublime Text (Code Editor) and Jupyter-Notebook (Data Analysis and Engineering) 
- Ubuntu 20.04+ (OS)

### You can run the project by running the following command (inside the code/ folder):
Before you run the code, make sure to set your sql instance configurations if you want to connect to other DB service provider or LocalDB in the following file:
```python
code/configurations/SQL_Config.py
``` 
Then after adding your configurations (Or if you want to use SQLite3 as your storge db edit/add on the transferData.py file) and downloaded needed packages (requirements.txt), excute the code script to transfer data in the db (the dataset is scheduled to automatic download and transfer it to the db using the github action schedule every day at 12pm riyadh time and you can change in this file (.github/workflows/main-analysis.yml)):
```python
python3 code/transferData.py
```
### Link To The Dashboard:
<table class="tg">
  <tr>
    <th class="tg-yw4l"><b>Name</b></th>
    <th class="tg-yw4l"><b>Description</b></th>
    <th class="tg-yw4l"><b>Link</b></th>
  </tr>
  
  <tr>
    <td class="tg-yw4l">Covid Dashboard</td>
    <td class="tg-yw4l">Dashboard of Saudi Arabia Cases and vaccinations rates in real-time</td>
    <td class="tg-yw4l">Dashboard<a href="#">
      <p>#</p>
    </a></td>
  </tr>
</table>
