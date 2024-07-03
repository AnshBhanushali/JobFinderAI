import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class JobRecommendationModel:
    def __init__(self):
        db_user = os.getenv('POSTGRES_USER')
        db_password = os.getenv('POSTGRES_PASSWORD')
        db_name = os.getenv('POSTGRES_DB')
        db_host = 'localhost'  # Use 'localhost' since Docker is not used

        if not db_user or not db_password or not db_name:
            raise Exception("Database environment variables not set correctly")

        self.engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}')
        
        self.jobs = pd.read_sql('jobs', self.engine)
        
        self.jobs = self.jobs.dropna(subset=['description'])

        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.job_vectors = self.vectorizer.fit_transform(self.jobs['description'])
        
    def recommend_jobs(self, resume, top_n=10):
        user_vector = self.vectorizer.transform([resume])

        similarities = cosine_similarity(user_vector, self.job_vectors).flatten()
        
        top_n_indices = similarities.argsort()[-top_n:][::-1]
        top_n_jobs = self.jobs.iloc[top_n_indices]
        
        return top_n_jobs.to_dict(orient='records')
