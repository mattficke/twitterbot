import psycopg2
import os
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

def write(num):
    conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)
    cur = conn.cursor()
    SQL = "INSERT INTO tweets (user_mentions_id) VALUES (%s);"
    data = [num]
    cur.execute(SQL, data)
    conn.commit()
    cur.close()
    conn.close()
    
def read():
    conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)
    cur = conn.cursor()
    SQL = "SELECT user_mentions_id FROM tweets;"
    cur.execute(SQL)
    result = cur.fetchall()
    enumerated = [i[0] for i in result]
    return enumerated
    
    cur.close()
    conn.close()