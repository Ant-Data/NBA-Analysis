import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# load database credentials from .env file
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# read csv
df = pd.read_csv("C:/Users/antho/Downloads/Data_analysis/NBA_data/data/nba_data.csv")

# connect to local postgreSQL
local_engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# neon connection string
neon_conn_str = ""
neon_engine = create_engine(neon_conn_str)

# Upload to database
df.to_sql('nba_stats', neon_engine, if_exists='replace', index=False)

print("✅ Data uploaded to PostgreSQL successfully.")


query = "SELECT team_location, team_name, athlete_display_name, points, opponent_team_location, opponent_team_name FROM nba_stats WHERE points > 30 "
df_test = pd.read_sql_query(query, con=local_engine)


df_test.to_sql("2012_points", neon_engine, index=False, if_exists="replace")


