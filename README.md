# Pre-requisites:
- Python installed
    - flask installed
    - pandas installed

# How to run
- load data to database
    - Command: python load_pop_data.py
- check if 'stats_can_population.sqlite' file has been generated
- if it is generated, run the server
    - Command: python server.py

# Contents
- population.csv 
    Data of Q4 2023 per province from Statistics Canada
    Source : https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901&cubeTimeFrame.startMonth=10&cubeTimeFrame.startYear=2023&cubeTimeFrame.endMonth=10&cubeTimeFrame.endYear=2023&referencePeriods=20231001%2C20231001

- load_pop_data.py
    The 'load_data.py' loads the 'population.csv' into the SQLite Database

- select_highest_pop_province.py
    A select query to return the highest populated province

- server.py
    Contains the backend (API)

- stats_can_population.sqlite


