## Job Recommendation System

This is a full-stack application that provides job recommendations based on user-submitted resumes. The project uses a Flask backend for handling the recommendation logic and a React frontend for the user interface. Data is stored in a PostgreSQL database, and the application is containerized using Docker.

### Features

- **Resume Upload**: Users can paste their resumes into a text box.
- **Job Recommendations**: The system processes the resume and returns the most relevant job listings.
- **Responsive UI**: A clean and responsive interface built with React.

### Tech Stack

- **Backend**: Flask, SQLAlchemy, Pandas
- **Frontend**: React, Axios
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Deployment**: Docker Compose

### Getting Started

#### Prerequisites

- Python 3.12
- Node.js and npm
- PostgreSQL
- Docker (optional)

#### Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/job-recommendation-system.git
   cd job-recommendation-system
   ```

2. **Backend Setup**:
   ```sh
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Database Setup**:
   Ensure PostgreSQL is installed and running.
   ```sh
   psql -U username -d postgres -f db/init.sql
   python3 data/load_data.py
   ```

4. **Run the Backend**:
   ```sh
   python3 app.py
   ```

5. **Frontend Setup**:
   ```sh
   cd ../frontend
   npm install
   npm start
   ```

6. **Access the Application**:
   - Frontend: `http://localhost:3000`
   - Backend: `http://localhost:5000`


### Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

### License

This project is licensed under the MIT License.
