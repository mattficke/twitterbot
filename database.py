import psycopg2
import os

DATABASE_URL = os.environ['DATABASE_URL']

def write(num):
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    SQL = "INSERT INTO tweets (user_mentions_id) VALUES (%s);"
    data = [num]
    cur.execute(SQL, data)
    conn.commit()
    cur.close()
    conn.close()
    
def read():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    SQL = "SELECT user_mentions_id FROM tweets;"
    cur.execute(SQL)
    result = cur.fetchall()
    enumerated = [i[0] for i in result]
    return enumerated
    
    cur.close()
    conn.close()