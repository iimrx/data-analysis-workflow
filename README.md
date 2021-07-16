# Covid-19 Dashboard
Self Challenge To Build Dashboard for Covid-19 and Analyzing it using Google Data Studio.
### Tech Used in This Challenge:
- SQL Database(SQLlite3), Google Cloud SQL (MSSQL)
   - Storge, Backuup
- Google Data Studio (Dashboard)
- Github Actions (CI/CD) 
- Python 3.8+ (Language)
   - All Packages Used Found In : requirements.txt
- Sublime Text (Code Editor) and Jupyter-Notebook (Data Analysis and Engineering) 
- Ubuntu 20.04+ (OS)
### You can run the project by running the following command (inside the project root):
Before you run the code, make sure to set your cloud sql instance configurations if you want to connect to other DB service provider or LocalDB in the following file:
```python
nano code/configurations/SQL_Config.py
```
Then after adding your configurations and downloaded needed packages(requirements.txt), excute the main code script (the dataset is scheduled to automatic download using the github action):
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
