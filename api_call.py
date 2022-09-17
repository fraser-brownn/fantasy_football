import pandas as pd
import numpy as np
import requests 
import psycopg2
import psycopg2.extras as extras
from datetime import date
import os

def add_date_inserted_column(dfs):
    for i in dfs:
        i['date_inserted'] = date.today()


def api_call():
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    r = requests.get(url)
    json = r.json()

    elements_df = pd.DataFrame(json['elements'])
    elements_types_df = pd.DataFrame(json['element_types'])
    teams_df = pd.DataFrame(json['teams'])
    events_df = pd.DataFrame(json['events'])

    events_df.drop("chip_plays", axis=1, inplace=True) #### REMOVE COLUMN WITH NESTED JSON, INFORMATION NOT REQUIRED FOR NOW
    events_df.drop('top_element_info', axis=1, inplace = True) #### REMOVE COLUMN WITH NESTED JSON, INFORMATION NOT REQUIRED FOR NOW

    teams_df = teams_df.rename(columns = {'name':'name_'}) ### CHANGED COLUMN NAME BECAUSE COMMAND IN SQL
    events_df = events_df.rename(columns = {'name':'name_'}) ### CHANGED COLUMN NAME BECAUSE COMMAND IN SQL

    elements_df = elements_df.rename(columns = {'id':'id_'}) ### CHANGED COLUMN NAME BECAUSE COMMAND IN SQL
    elements_types_df = elements_types_df.rename(columns = {'id':'id_'}) ### CHANGED COLUMN NAME BECAUSE COMMAND IN SQL

    dfs = [elements_df, elements_types_df, teams_df, events_df]
    add_date_inserted_column(dfs)
    return  dfs