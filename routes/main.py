# app/routes/main_routes.py

import time

import pandas as pd
from flask import Blueprint, render_template, make_response, jsonify
from sqlalchemy import func

from models.Circuits import *
from models.db import get_db, query_db

main = Blueprint("main", __name__)


@main.route("/")
def home():
    # first_circuit = db.session.query(Circuits).first()
    # print(first_circuit)
    # Randomly select a circuit
    circuit = Circuits.query.order_by(func.random()).first()

    print(circuit)
    return render_template("pages/index.html")


# Create a route to make users login
@main.route("/login")
def login():
    return render_template("pages/login.html")


@main.route('/time')
def get_current_time():
    return {'time': time.time()}


@main.route('/circuit/<circuit_id>')
def get_circuit_info(circuit_id):
    circuit = Circuits.query.filter_by(circuit_id=circuit_id).first()
    return make_response(jsonify(circuit), 200)


@main.route('/circuit')
def get_circuit():
    conn = get_db()
    query = """
    SELECT *
    FROM circuits
    ORDER BY RANDOM()
    LIMIT 1
    """
    val = query_db(query, one=True)

    res = {key: val[key] for key in val.keys()}
    return make_response(jsonify(res), 200)


@main.route('/performance')
def get_performance():
    # Get qualifying results and race results
    conn = get_db()
    query = """
    SELECT 
        forename, surname, COUNT(r.position) as "totalWins"
    FROM
        drivers d
    JOIN results r on d.driverId = r.driverId
    WHERE r.position = 1
    GROUP BY forename, surname
    ORDER BY totalWins DESC 
    """
    # Print the first qualifying result that matches
    df = pd.read_sql(query, conn)
    df['name'] = df['forename'] + ' ' + df['surname']
    df = df[['name', 'totalWins']]

    # Make response
    response = make_response(df.to_json(orient='records'), 200)
    response.headers['Content-Type'] = 'application/json'

    return response


@main.route('/positions/average')
def avg_position():
    conn = get_db()
    query = """
    SELECT 
        d.forename, 
        d.surname, 
        r2.year, 
        AVG(r.position) as "averagePos"
    FROM drivers d
    JOIN results r ON d.driverId = r.driverId
    JOIN races r2 ON r.raceId = r2.raceId
    GROUP BY d.forename, d.surname, r2.year"""
    df = pd.read_sql(query, conn)
    df['name'] = df['forename'] + ' ' + df['surname']
    df = df[['name', 'year', 'averagePos']]

    # Make response
    response = make_response(df.to_json(orient='records'), 200)
    response.headers['Content-Type'] = 'application/json'

    return response