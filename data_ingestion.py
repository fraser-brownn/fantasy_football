import pandas as pd
import numpy as np
import psycopg2
import psycopg2.extras as extras
from pulp import *


def execute_query(query):
    PASSWORD = os.environ.get('PGPASSWORD') 
    conn = psycopg2.connect(f"dbname=fantasy_football user=postgres password={PASSWORD}")
    cur = conn.cursor()
    cur.execute(query)
    column_names = [col_name[0] for col_name in cur.description]
    data = cur.fetchall()
    cur.close()
    conn.close()
    df = pd.DataFrame(data)
    df.columns = column_names
    return df
