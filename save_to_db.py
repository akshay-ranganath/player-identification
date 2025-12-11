# read the file cfl_players.csv and save the data to a sqlite database
# create the database if it doesn't exit
import sqlite3
import pandas as pd

df = pd.read_csv('cfl_players.csv')

conn = sqlite3.connect('cfl_players.db')
df.to_sql('cfl_players', conn, if_exists='replace', index=False)
conn.close()