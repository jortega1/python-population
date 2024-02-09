# Pre-requisites:
- ### Python installed
    - flask installed
    - pandas installed

# How to run
- ### load data to database
    - Command: **_python load_pop_data.py_**
    - Command: **_python load_immigrant_data_**
- ### check if _'stats_can_population.sqlite'_ and _'stats_can_immigrants.sqlite'_ file has been generated
- ### if it is generated, run the server
    - Command: **_python server.py_**

# Contents
- ### population.csv 
    Data of Q4 2023 per province from Statistics Canada
    Source : https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901&cubeTimeFrame.startMonth=10&cubeTimeFrame.startYear=2023&cubeTimeFrame.endMonth=10&cubeTimeFrame.endYear=2023&referencePeriods=20231001%2C20231001

- ### immigrants_alberta.csv
    Data of 2021 Alberta Population from Statistics Canada
    Source : https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/page.cfm?LANG=E&GENDERlist=1&STATISTIClist=1&DGUIDlist=2021A000248&HEADERlist=25&SearchText=Alberta

- ### immigrants_alberta_continent.csv
    Modified immigrants_alberta.csv (by continent)

- ### immigrants_alberta_country.csv
    Modified immigrants_alberta.csv (by country)

- ### load_pop_data.py
    The 'load_data.py' loads the 'population.csv' into the SQLite Database

- ### load_immigrants_data.py
    The 'load_immigrants_data.py' loads the different immigrant data into the SQLite Database

- ### server.py
    Contains the backend (API)


