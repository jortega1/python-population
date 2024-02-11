# Pre-requisites:
- ### Python installed
    - flask installed
    - pandas installed

# Tasks :
- ### Return what is most populated province in Canada? (Easy)
    This is answered by localhost:///population/most
- ### Return which country immigrants are born in Alberta (Advanced)
    This is answered by localhost:///immigrants/country/most

# How to use
- ### load data to database
    - Command: **_python load_pop_data.py_**
    - Command: **_python load_immigrant_data_**
- ### check if _'stats_can_population.sqlite'_ and _'stats_can_immigrants.sqlite'_ file has been generated
- ### if it is generated, run the server
    - Command: **_python server.py_**
- ### After running the server, to view the valid URLs go to, localhost:5000/urls

# Contents
- ### data
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

# Data
- ### The data used for _population.csv_ is from the link below. The data was not cleaned or modified.
    Data of Q4 2023 per province from Statistics Canada
    Source : https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901&cubeTimeFrame.startMonth=10&cubeTimeFrame.startYear=2023&cubeTimeFrame.endMonth=10&cubeTimeFrame.endYear=2023&referencePeriods=20231001%2C20231001

- ### The data used for -immigrants.csv_ is from the link below. The data was cleaned in order to be loeaded properly to the DB. The data used for _immigrants_alberta_continent.csv_ and _immigrants_alberta_country.csv_ is derived from _immigrants.csv_
    Data of 2021 Alberta Population from Statistics Canada
    Source : https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/page.cfm?LANG=E&GENDERlist=1&STATISTIClist=1&DGUIDlist=2021A000248&HEADERlist=25&SearchText=Alberta
