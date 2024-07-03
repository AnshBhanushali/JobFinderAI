from flask import Flask, request, jsonify
from flask_cors import CORS
from models.job_recomModel import JobRecommendationModel

app = Flask(__name__)
CORS(app)

job_model = JobRecommendationModel()

@app.route('/recommend', methods=['POST'])
def recommend():
    user_data = request.json
    user_resume = user_data['resume']

   
    recommendations = job_model.recommend_jobs(user_resume)

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
