import pandas as pd
import numpy as np
import requests 
import psycopg2
import psycopg2.extras as extras
from datetime import date
import os
from api_call import api_call



def insert_dataframes(conn, df, table):
    '''
    INSERTS DATAFRAMES INTO PRE BUILT SQL TABLES
    
    '''
  
    tuples = [tuple(x) for x in df.to_numpy()]
  
    cols = ', '.join(list(df.columns))
    # SQL query to execute
    query = "INSERT INTO %s (%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("the dataframe is inserted")
    cursor.close()

if __name__ == '__main__':  
    PASSWORD = os.environ.get('PGPASSWORD')  
    conn = psycopg2.connect(f"dbname=fantasy_football user=postgres password={PASSWORD}")

    elements_df, elements_types_df, teams_df, events_df = api_call()

    insert_dataframes(conn, elements_df, 'fantasy_football')
    insert_dataframes(conn, elements_types_df, 'player_types')
    insert_dataframes(conn, teams_df, 'teams')
    insert_dataframes(conn, events_df, 'events')