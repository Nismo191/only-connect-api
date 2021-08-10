from app import app, sqlite_tools
from flask import Response
import json
import os

import sqlite3

version = "v1"

#Connect to sqlite database
def connect(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def select_all_from_table(conn, table):
    query = "SELECT * FROM " + table
    # conn.row_factory = sqlite3.Row
    # cur = conn.cursor()
    # cur.execute(query)

    # rows = cur.fetchall()
    # print(rows.keys())
    # print(tuple(rows))
    conn.row_factory = sqlite3.Row
    jsonData = {}
    for row in conn.execute(query):
        print(row.keys())
        print(tuple(row))
        jsonData[tuple(row)[0]] = {
                                    "id": tuple(row)[0], 
                                    "type": tuple(row)[1], 
                                    "clue1": tuple(row)[2], 
                                    "clue2": tuple(row)[3], 
                                    "clue3": tuple(row)[4], 
                                    "clue4": tuple(row)[5], 
                                    "answer": tuple(row)[6], 
                                    "series": tuple(row)[7], 
                                    "episode": tuple(row)[8]
                                }
    return jsonData

def select_id_from_table(conn, table, id):
    query = "SELECT * FROM " + table + " WHERE id = " + str(id)
    # conn.row_factory = sqlite3.Row
    # cur = conn.cursor()
    # cur.execute(query)

    # rows = cur.fetchall()
    # print(rows.keys())
    # print(tuple(rows))
    conn.row_factory = sqlite3.Row
    jsonData = {}
    for row in conn.execute(query):
        print(row.keys())
        print(tuple(row))
        jsonData[tuple(row)[0]] = {
                                    "id": tuple(row)[0], 
                                    "type": tuple(row)[1], 
                                    "clue1": tuple(row)[2], 
                                    "clue2": tuple(row)[3], 
                                    "clue3": tuple(row)[4], 
                                    "clue4": tuple(row)[5], 
                                    "answer": tuple(row)[6], 
                                    "series": tuple(row)[7], 
                                    "episode": tuple(row)[8]
                                }
    return jsonData

def select_series_episode_from_table(conn, table, series, episode):
    query = "SELECT * FROM " + table + " WHERE series = " + str(series) + " AND episode = " + str(episode)
    # conn.row_factory = sqlite3.Row
    # cur = conn.cursor()
    # cur.execute(query)

    # rows = cur.fetchall()
    # print(rows.keys())
    # print(tuple(rows))
    conn.row_factory = sqlite3.Row
    jsonData = {}
    for row in conn.execute(query):
        print(row.keys())
        print(tuple(row))
        jsonData[tuple(row)[0]] = {
                                    "id": tuple(row)[0], 
                                    "type": tuple(row)[1], 
                                    "clue1": tuple(row)[2], 
                                    "clue2": tuple(row)[3], 
                                    "clue3": tuple(row)[4], 
                                    "clue4": tuple(row)[5], 
                                    "answer": tuple(row)[6], 
                                    "series": tuple(row)[7], 
                                    "episode": tuple(row)[8]
                                }
    return jsonData



def select_all_connecting_walls_from_table(conn, table):
    query = sqlite_tools.return_connecting_wall_sql()
    # conn.row_factory = sqlite3.Row
    # cur = conn.cursor()
    # cur.execute(query)

    # rows = cur.fetchall()
    # print(rows.keys())
    # print(tuple(rows))
    conn.row_factory = sqlite3.Row
    jsonData = {}
    for row in conn.execute(query):
        print(row.keys())
        print(tuple(row))
        jsonData[tuple(row)[0]] = {
                                    "id": tuple(row)[0], 
                                    "row1_id": tuple(row)[1], 
                                    "sec1_item1": tuple(row)[2], 
                                    "sec1_item2": tuple(row)[3], 
                                    "sec1_item3": tuple(row)[4], 
                                    "sec1_item4": tuple(row)[5], 
                                    "section1_answer": tuple(row)[6],
                                    "row2_id": tuple(row)[7], 
                                    "sec2_item1": tuple(row)[8], 
                                    "sec2_item2": tuple(row)[9], 
                                    "sec2_item3": tuple(row)[10], 
                                    "sec2_item4": tuple(row)[11], 
                                    "section2_answer": tuple(row)[12],
                                    "row3_id": tuple(row)[13], 
                                    "sec3_item1": tuple(row)[14], 
                                    "sec3_item2": tuple(row)[15], 
                                    "sec3_item3": tuple(row)[16], 
                                    "sec3_item4": tuple(row)[17], 
                                    "section3_answer": tuple(row)[18],
                                    "row4_id": tuple(row)[19], 
                                    "sec4_item1": tuple(row)[20], 
                                    "sec4_item2": tuple(row)[21], 
                                    "sec4_item3": tuple(row)[22], 
                                    "sec4_item4": tuple(row)[23], 
                                    "section4_answer": tuple(row)[24], 
                                    "series": tuple(row)[25], 
                                    "episode": tuple(row)[26]
                                }
    return jsonData

def select_id_connecting_walls_from_table(conn, table, id):
    query = sqlite_tools.return_connecting_wall_sql()
    query = query + " WHERE cw.id = " + str(id)
    # conn.row_factory = sqlite3.Row
    # cur = conn.cursor()
    # cur.execute(query)

    # rows = cur.fetchall()
    # print(rows.keys())
    # print(tuple(rows))
    conn.row_factory = sqlite3.Row
    jsonData = {}
    for row in conn.execute(query):
        print(row.keys())
        print(tuple(row))
        jsonData[tuple(row)[0]] = {
                                    "id": tuple(row)[0], 
                                    "row1_id": tuple(row)[1], 
                                    "sec1_item1": tuple(row)[2], 
                                    "sec1_item2": tuple(row)[3], 
                                    "sec1_item3": tuple(row)[4], 
                                    "sec1_item4": tuple(row)[5], 
                                    "section1_answer": tuple(row)[6],
                                    "row2_id": tuple(row)[7], 
                                    "sec2_item1": tuple(row)[8], 
                                    "sec2_item2": tuple(row)[9], 
                                    "sec2_item3": tuple(row)[10], 
                                    "sec2_item4": tuple(row)[11], 
                                    "section2_answer": tuple(row)[12],
                                    "row3_id": tuple(row)[13], 
                                    "sec3_item1": tuple(row)[14], 
                                    "sec3_item2": tuple(row)[15], 
                                    "sec3_item3": tuple(row)[16], 
                                    "sec3_item4": tuple(row)[17], 
                                    "section3_answer": tuple(row)[18],
                                    "row4_id": tuple(row)[19], 
                                    "sec4_item1": tuple(row)[20], 
                                    "sec4_item2": tuple(row)[21], 
                                    "sec4_item3": tuple(row)[22], 
                                    "sec4_item4": tuple(row)[23], 
                                    "section4_answer": tuple(row)[24], 
                                    "series": tuple(row)[25], 
                                    "episode": tuple(row)[26]
                                }
    return jsonData

def select_series_episode_connecting_walls_from_table(conn, table, series, episode):
    query = sqlite_tools.return_connecting_wall_sql()
    query = query + " WHERE series = " + str(series) + " AND episode = " + str(episode)
    # conn.row_factory = sqlite3.Row
    # cur = conn.cursor()
    # cur.execute(query)

    # rows = cur.fetchall()
    # print(rows.keys())
    # print(tuple(rows))
    conn.row_factory = sqlite3.Row
    jsonData = {}
    for row in conn.execute(query):
        print(row.keys())
        print(tuple(row))
        jsonData[tuple(row)[0]] = {
                                    "id": tuple(row)[0], 
                                    "row1_id": tuple(row)[1], 
                                    "sec1_item1": tuple(row)[2], 
                                    "sec1_item2": tuple(row)[3], 
                                    "sec1_item3": tuple(row)[4], 
                                    "sec1_item4": tuple(row)[5], 
                                    "section1_answer": tuple(row)[6],
                                    "row2_id": tuple(row)[7], 
                                    "sec2_item1": tuple(row)[8], 
                                    "sec2_item2": tuple(row)[9], 
                                    "sec2_item3": tuple(row)[10], 
                                    "sec2_item4": tuple(row)[11], 
                                    "section2_answer": tuple(row)[12],
                                    "row3_id": tuple(row)[13], 
                                    "sec3_item1": tuple(row)[14], 
                                    "sec3_item2": tuple(row)[15], 
                                    "sec3_item3": tuple(row)[16], 
                                    "sec3_item4": tuple(row)[17], 
                                    "section3_answer": tuple(row)[18],
                                    "row4_id": tuple(row)[19], 
                                    "sec4_item1": tuple(row)[20], 
                                    "sec4_item2": tuple(row)[21], 
                                    "sec4_item3": tuple(row)[22], 
                                    "sec4_item4": tuple(row)[23], 
                                    "section4_answer": tuple(row)[24], 
                                    "series": tuple(row)[25], 
                                    "episode": tuple(row)[26]
                                }
    return jsonData


def select_all_missing_vowels_from_table(conn, table):
    query = "SELECT * FROM " + table
    # conn.row_factory = sqlite3.Row
    # cur = conn.cursor()
    # cur.execute(query)

    # rows = cur.fetchall()
    # print(rows.keys())
    # print(tuple(rows))
    conn.row_factory = sqlite3.Row
    jsonData = {}
    for row in conn.execute(query):
        print(row.keys())
        print(tuple(row))
        jsonData[tuple(row)[0]] = {
                                    "id": tuple(row)[0], 
                                    "missing": tuple(row)[1], 
                                    "complete": tuple(row)[2], 
                                    "category": tuple(row)[3], 
                                    "series": tuple(row)[4], 
                                    "episode": tuple(row)[5]
                                }
    return jsonData

def select_id_missing_vowels_from_table(conn, table, id):
    query = "SELECT * FROM " + table + " WHERE id = " + str(id)
    # conn.row_factory = sqlite3.Row
    # cur = conn.cursor()
    # cur.execute(query)

    # rows = cur.fetchall()
    # print(rows.keys())
    # print(tuple(rows))
    conn.row_factory = sqlite3.Row
    jsonData = {}
    for row in conn.execute(query):
        print(row.keys())
        print(tuple(row))
        jsonData[tuple(row)[0]] = {
                                    "id": tuple(row)[0], 
                                    "missing": tuple(row)[1], 
                                    "complete": tuple(row)[2], 
                                    "category": tuple(row)[3], 
                                    "series": tuple(row)[4], 
                                    "episode": tuple(row)[5]
                                }
    return jsonData

def select_series_episode_missing_vowels_from_table(conn, table, series, episode):
    query = "SELECT * FROM " + table + " WHERE series = " + str(series) + " AND episode = " + str(episode)
    # conn.row_factory = sqlite3.Row
    # cur = conn.cursor()
    # cur.execute(query)

    # rows = cur.fetchall()
    # print(rows.keys())
    # print(tuple(rows))
    conn.row_factory = sqlite3.Row
    jsonData = {}
    for row in conn.execute(query):
        print(row.keys())
        print(tuple(row))
        jsonData[tuple(row)[0]] = {
                                    "id": tuple(row)[0], 
                                    "missing": tuple(row)[1], 
                                    "complete": tuple(row)[2], 
                                    "category": tuple(row)[3], 
                                    "series": tuple(row)[4], 
                                    "episode": tuple(row)[5]
                                }
    return jsonData


def init():
    db = r"C:\Users\nismo\Documents\Projects\OnlyConnect_API\only_connect.db"
    conn = connect(db)

    return conn

#Connections
@app.route('/api/'+version+'/connections/')
def connections():
    conn = init()
    data = select_all_from_table(conn, "connections")
    return Response(json.dumps(data),  mimetype='application/json')

@app.route('/api/'+version+'/connections/<int:id>/')
def connections_id(id):
    conn = init()
    data = select_id_from_table(conn, "connections", id)
    return Response(json.dumps(data),  mimetype='application/json')

@app.route('/api/'+version+'/connections/series_episode/<int:series>/<int:episode>/')
def connections_series_episode(series, episode):
    conn = init()
    data = select_series_episode_from_table(conn, "connections", series, episode)
    return Response(json.dumps(data),  mimetype='application/json')


#Sequences
@app.route('/api/'+version+'/sequences/')
def sequences():
    conn = init()
    data = select_all_from_table(conn, "sequences")
    return Response(json.dumps(data),  mimetype='application/json')

@app.route('/api/'+version+'/sequences/<int:id>/')
def sequences_id(id):
    conn = init()
    data = select_id_from_table(conn, "sequences", id)
    return Response(json.dumps(data),  mimetype='application/json')

@app.route('/api/'+version+'/sequences/series_episode/<int:series>/<int:episode>/')
def sequences_series_episode(series, episode):
    conn = init()
    data = select_series_episode_from_table(conn, "sequences", series, episode)
    return Response(json.dumps(data),  mimetype='application/json')


#Connecting Walls
@app.route('/api/'+version+'/connecting_walls/')
def connecting_walls():
    conn = init()
    data = select_all_connecting_walls_from_table(conn, "connecting_walls")
    return Response(json.dumps(data),  mimetype='application/json')

@app.route('/api/'+version+'/connecting_walls/<int:id>/')
def connecting_walls_id(id):
    conn = init()
    data = select_id_connecting_walls_from_table(conn, "connecting_walls", id)
    return Response(json.dumps(data),  mimetype='application/json')

@app.route('/api/'+version+'/connecting_walls/series_episode/<int:series>/<int:episode>/')
def connecting_walls_series_episode(series, episode):
    conn = init()
    data = select_series_episode_connecting_walls_from_table(conn, "connecting_walls", series, episode)
    return Response(json.dumps(data),  mimetype='application/json')


#Missing Vowels
@app.route('/api/'+version+'/missing_vowels/')
def missing_vowels():
    conn = init()
    data = select_all_missing_vowels_from_table(conn, "missing_vowels")
    return Response(json.dumps(data),  mimetype='application/json')

@app.route('/api/'+version+'/missing_vowels/<int:id>/')
def missing_vowels_id(id):
    conn = init()
    data = select_id_missing_vowels_from_table(conn, "missing_vowels", id)
    return Response(json.dumps(data),  mimetype='application/json')

@app.route('/api/'+version+'/missing_vowels/series_episode/<int:series>/<int:episode>/')
def missing_vowels_series_episode(series, episode):
    conn = init()
    data = select_series_episode_missing_vowels_from_table(conn, "missing_vowels", series, episode)
    return Response(json.dumps(data),  mimetype='application/json')

