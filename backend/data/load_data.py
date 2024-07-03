import pandas as pd
from sqlalchemy import create_engine
import os

# database connection
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_name = os.getenv('POSTGRES_DB')
db_host = 'db'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}')