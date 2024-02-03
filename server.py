from flask import Flask, jsonify
import pandas as pd
import sqlite3


# Instantiate server
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'go to http://127.0.0.1:5000/mostpopulated'

@app.route('/mostpopulated')
def mostpopulated():
    conn = sqlite3.connect('stats_can_population.sqlite')
    sql = pd.read_sql('SELECT GEO as PROVINCE, MAX(VALUE) as POPULATION FROM population WHERE VALUE < (SELECT MAX(VALUE) FROM population)', conn)
    return sql.to_json(orient='records')