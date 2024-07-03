import pandas as pd
from sqlalchemy import create_engine
import os

# database connection
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_name = os.getenv('POSTGRES_DB')
db_host = 'db'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}')

# data from CSV
jobs_df = pd.read_csv('backend/data/jobs.csv')

# Manipulating data from csv
jobs_df = jobs_df[['Job Title', 'Key Skills', 'Role Category', 'Location']]
jobs_df.columns = ['title', 'description', 'company', 'location']

jobs_df['company'] = jobs_df['company'] + " - " + jobs_df['description']

jobs_df.drop_duplicates(inplace=True)

jobs_df.to_sql('jobs', engine, if_exists='replace', index=False)

print("Data has been successfully inserted into the database.")


