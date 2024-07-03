import React, { useState } from 'react';
import axios from 'axios';
import './JobRecommendation.css'; 

const JobRecommendation = () => {
    const [resume, setResume] = useState('');
    const [jobs, setJobs] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:5000/recommend', { resume });
            setJobs(response.data);
        } catch (error) {
            console.error('Error fetching job recommendations:', error);
        }
    };

    return (
        <div className="job-recommendation">
            <h1>Job Recommendations</h1>
            <form onSubmit={handleSubmit} className="resume-form">
                <textarea
                    value={resume}
                    onChange={(e) => setResume(e.target.value)}
                    placeholder="Paste your resume here"
                    rows="10"
                    cols="50"
                    required
                />
                <button type="submit">Get Recommendations</button>
            </form>
            <ul className="job-list">
                {jobs.map((job, index) => (
                    <li key={index} className="job-item">
                        <h2>{job.title}</h2>
                        <p>{job.description}</p>
                        <p><strong>Company:</strong> {job.company}</p>
                        <p><strong>Location:</strong> {job.location}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default JobRecommendation;
