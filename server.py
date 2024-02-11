from flask import Flask, request, jsonify
import pandas as pd
import sqlite3

# Instantiate server
app = Flask(__name__)

# Connect to DB
def conn_to_db(db):
    return sqlite3.connect(db)

# Create cursor and set row factory for sqlite3
def create_cursor(conn):
    conn.row_factory = sqlite3.Row
    return conn.cursor()

@app.route('/urls', methods=['GET'])
def welcome():
    valid_url = []
    u1 = {
            'url': '/population',
            'URL Function' : 'Lists all population in Canada by province' 
        }
    u2 = {
            'url': '/population?province=<valid_province>',
            'URL Function' : 'Lists the population of the chosen province' 
        }
    u3 = {
            'url': '/population/most',
            'URL Function' : 'Lists the most populated province' 
        }
    u4 = {
            'url': '/immigrants/continents',
            'URL Function' : 'Lists the population in Alberta of immigrants ordered by which continent they are born' 
        }
    u5 = {
            'url': '/immigrants/continents?continent=<valid_continent>',
            'URL Function' : 'Lists the population in Alberta of immigrants with chosen continent' 
        }
    u6 = {
            'url': '/immigrants/continents/most',
            'URL Function' : 'Lists the continent and population in Alberta where most immigrants are born from'
        }

    u7 = {
            'url': '/immigrants/countries',
            'URL Function' : 'Lists the population in Alberta of immigrants ordered by which country they are born' 
        }
    u8 = {
            'url': '/immigrants/country?country=<valid_country>',
            'URL Function' : 'Lists the population in Alberta of immigrants with chosen continent' 
        }
    u9 = {
            'url': '/immigrants/country/most',
            'URL Function' : 'Lists the country and population in Alberta where most immigrants are born from'
        }
    valid_url.append(u1)
    valid_url.append(u2)
    valid_url.append(u3)
    valid_url.append(u4) 
    valid_url.append(u5)
    valid_url.append(u6)
    valid_url.append(u7)
    valid_url.append(u8)
    valid_url.append(u9)

    return jsonify(valid_url)

@app.route('/population', methods=['GET'])
def population():
    population_data = []
    try: 
        conn = conn_to_db('stats_can_population.sqlite')
        cur = create_cursor(conn)

        province = request.args.get('province')
        
        if province is None :
            cur.execute('SELECT * FROM population')
        else :
            cur.execute('SELECT * FROM population WHERE GEO = ?', (province,))

        rows = cur.fetchall()
        for row in rows:
            population = {}
            population['Province'] = row['GEO']
            population['Population'] = row['VALUE']
            population_data.append(population)

        conn.close()
    except Exception as e :
        return f'Error: {e}'
    if not population_data:
        return "Invalid province, check value"
    else:
        return jsonify(population_data)
    
@app.route('/population/most', methods=['GET'])
def most_population():
    most_populated = []
    try: 
        conn = conn_to_db('stats_can_population.sqlite')
        cur = create_cursor(conn)

        cur.execute('SELECT GEO, MAX(VALUE) as VALUE FROM population WHERE VALUE < (SELECT MAX(VALUE) FROM population)')

        rows = cur.fetchall()
        for row in rows:
            population = {}
            population['Province'] = row['GEO']
            population['Population'] = row['VALUE']
            most_populated.append(population)

        conn.close()
    except Exception as e :
        return f'Error: {e}'
    return jsonify(most_populated)

@app.route('/immigrants/continents', methods=['GET'])
def ab_immigrants_continents():
    immigrants = []
    try:
        conn = conn_to_db('stats_can_immigrant.sqlite')
        cur = create_cursor(conn)

        cur.execute('SELECT * FROM immigrants_alberta_continent')

        continent = request.args.get('continent')
        
        if continent is None :
            cur.execute('SELECT * FROM immigrants_alberta_continent')
        else :
            cur.execute('SELECT * FROM immigrants_alberta_continent WHERE Continent = ?', (continent,))

        rows = cur.fetchall()
        for row in rows:
            immigrant = {}
            immigrant['Continent'] = row['Continent']
            immigrant['Population'] = row['Population']
            immigrants.append(immigrant)

        conn.close()
    except Exception as e:
        return f'Error: {e}'
    if not immigrants:
        return "Invalid continent, check value"
    else:
        return jsonify(immigrants)
    
@app.route('/immigrants/continent/most', methods=['GET'])
def ab_immigrants_continent_most():
    immigrants = []
    try:
        conn = conn_to_db('stats_can_immigrant.sqlite')
        cur = create_cursor(conn)

        cur.execute('SELECT Continent, MAX(Population) as Population FROM immigrants_alberta_continent')

        rows = cur.fetchall()
        for row in rows:
            immigrant = {}
            immigrant['Continent'] = row['Continent']
            immigrant['Population'] = row['Population']
            immigrants.append(immigrant)

        conn.close()
    except Exception as e:
        return f'Error: {e}'
    return jsonify(immigrants)

@app.route('/immigrants/countries', methods=['GET'])
def ab_immigrants_countries():
    immigrants = []
    try:
        conn = conn_to_db('stats_can_immigrant.sqlite')
        cur = create_cursor(conn)

        cur.execute('SELECT * FROM immigrants_alberta_continent')

        country = request.args.get('country')
        
        if country is None :
            cur.execute('SELECT * FROM immigrants_alberta_country')
        else :
            cur.execute('SELECT * FROM immigrants_alberta_country WHERE Country = ?', (country,))

        rows = cur.fetchall()
        for row in rows:
            immigrant = {}
            immigrant['Country'] = row['Country']
            immigrant['Population'] = row['Population']
            immigrants.append(immigrant)

        conn.close()
    except Exception as e:
        return f'Error: {e}'
    if not immigrants:
        return "Invalid continent, check value"
    else:
        return jsonify(immigrants)
    
@app.route('/immigrants/countries/most', methods=['GET'])
def ab_immigrants_countries_most():
    immigrants = []
    try:
        conn = conn_to_db('stats_can_immigrant.sqlite')
        cur = create_cursor(conn)

        cur.execute('SELECT Country, MAX(Population) as Population FROM immigrants_alberta_country')

        rows = cur.fetchall()
        for row in rows:
            immigrant = {}
            immigrant['Country'] = row['Country']
            immigrant['Population'] = row['Population']
            immigrants.append(immigrant)

        conn.close()
    except Exception as e:
        return f'Error: {e}'
    return jsonify(immigrants)

if __name__ == "__main__":
    app.run(debug='TRUE')