# May 2024 - Software Engineering Project (Group 13)

IIT Madras Software Engineering Group Project - May 2024

## Padh.ai : Learning Management System with AI Integration

## Project Overview

This project is a Learning Management System (LMS) with integrated generative AI capabilities. It's designed to provide a comprehensive learning platform for students, enhanced with AI-powered features for a more engaging & enriching study experience.

## Features

- User authentication and authorization
- Support for video lectures
- Assignment handling:
  - Multiple-choice questions (MCQ) based Assignments
  - Programming assignments with automatic evaluation
- AI-powered chat system for student support
- AI-powered lecture summaries for a concise overview
- Support for creating and editing notes
- Progress tracking and grading system
- RESTful API for easy integration with front-end applications

## Technologies Used

- Backend: Python with Flask framework
- Database: SQLite with SQLAlchemy ORM
- API: Flask-RestX for RESTful API development
- Authentication: Flask-JWT-Extended for JSON Web Token authentication
- Code Execution: Piston API for remote code execution and evaluation
- AI Integration: Gemini Flash 1.5
- Frontend: Vue.js, vuelidate, axios, vue-ace-editor, bootstrap, vue-router

## Project Folder Structure

```
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── utils/
│   ├── config.py
│   ├── instance
│   │   ├── db.sqlite3
│   │   └── test_db.sqlite3
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── run.py
│   └── tests/
├── frontend/
│   └── padh.ai/
│       ├── eslintrc.cjs
│       ├── index.html
│       ├── jsconfig.json
│       ├── package.json
│       ├── package-lock.json
│       ├── prettierrc.json
│       ├── public/
│       │   └── favicon.ico
│       ├── README.md
│       ├── src/
│       │   ├── App.vue
│       │   ├── assets/
│       │   ├── components/
│       │   ├── main.js
│       │   ├── router/
│       │   └── views/
│       └── vite.config.js
├── package-lock.json
└── README.md
```

## Setup and Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/gagneetkaur04/soft-engg-project-may-2024-se-may-13.git
   cd soft-engg-project-may-2024-se-may-13
   ```

2. Set up a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root of the backend directory and add the following variables:

   ```sh
   GEMINI_API_KET=your_gemini_key
   ```

5. Run the application:

   ```sh
   python3 run.py
   ```

   The API should now be running on `http://localhost:5000`.

6. Setup and Installation of npm packages for frontend.

   ```sh
   cd frontend/padh.ai/
   npm install
   ```

7. Run the following command to start the frontend server in dev mode

   ```sh
   npm run dev
   ```

## API Documentation

Once the application is running, you can access the Swagger UI documentation at `http://localhost:5000/docs`. This provides a comprehensive overview of all available endpoints and allows for easy testing.

## Testing

We use pytest for testing in our project. To run the test suite, make sure you're in the backend directory and run:

```sh
pytest -v
```

This will give you the status of all the test cases in the project.
