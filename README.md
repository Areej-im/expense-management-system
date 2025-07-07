# Expense Management System
This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/areej-im/expense-management-system
cd expense-management-system

pip install -r requirements.txt

uvicorn server.server:app --reload

streamlit run frontend/app.py


