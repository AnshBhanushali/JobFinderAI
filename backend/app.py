from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy import create_engine
import os

app = Flask(__name__)
CORS(app)

# Database connection
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_name = os.getenv('POSTGRES_DB')
db_host = 'db'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}')

# Load Datasets
jobs = pd.read_sql('jobs', engine)

# Vectorize job description
vectorizer = TfidfVectorizer(stop_words='english')
job_vectors = vectorizer.fit_transform(jobs['description'])

@app.route('/recommend', methods=['POST'])
def recommend():
    user_data = request.json
    user_resume = user_data['resume']

    user_vector = vectorizer.transform([user_resume])
    similarities = cosine_similarity(user_vector, job_vectors).flatten()

    top_n_indices = similarities.argsort()[-10:][::-1]
    top_n_jobs = jobs.iloc[top_n_indices]

    return jsonify(top_n_jobs.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)