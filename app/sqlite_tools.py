import sqlite3
from flask import jsonify

#Connect to sqlite database
def connect(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def select_all_from_table(conn, table):
    query = "SELECT * FROM " + table
    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()

    return rows


def return_connecting_wall_sql():
    query = """SELECT 
                cw.id,
                section1 as row1_id,
                cws1.item1 as sec1_item1,
                cws1.item2 as sec1_item2,
                cws1.item3 as sec1_item3,
                cws1.item4 as sec1_item4,
                section1_answer,
                section2 as row2_id,
                cws2.item1 as sec2_item1,
                cws2.item2 as sec2_item2,
                cws2.item3 as sec2_item3,
                cws2.item4 as sec2_item4,
                section2_answer,
                section3 as row3_id,
                cws3.item1 as sec3_item1,
                cws3.item2 as sec3_item2,
                cws3.item3 as sec3_item3,
                cws3.item4 as sec3_item4,
                section3_answer,
                section4 as row4_id,
                cws4.item1 as sec4_item1,
                cws4.item2 as sec4_item2,
                cws4.item3 as sec4_item3,
                cws4.item4 as sec4_item4,
                section4_answer,
                cw.series,
                cw.episode
                from connecting_walls as cw
                INNER JOIN connecting_walls_section as cws1
                on cw.section1 = cws1.id
                INNER JOIN connecting_walls_section as cws2
                on cw.section2 = cws2.id
                INNER JOIN connecting_walls_section as cws3
                on cw.section3 = cws3.id
                INNER JOIN connecting_walls_section as cws4
                on cw.section4 = cws4.id"""

    return query


if __name__ == '__main__':
    db_file = r"C:\Users\nismo\Documents\Projects\OnlyConnect_API\only_connect.db"
    conn = connect(db_file)
    data = select_all_from_table(conn, "connections")
    print(jsonify(data))

