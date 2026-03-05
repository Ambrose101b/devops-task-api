from fastapi import FastAPI

# Initialize the application
app = FastAPI(title="DevOps Task API")

# A simple in-memory "database" (a Python list of dictionaries)
# In a production app, this would be PostgreSQL or MySQL
tasks_db = [
    {"id": 1, "title": "Learn Docker", "completed": False},
    {"id": 2, "title": "Setup Jenkins Pipeline", "completed": False}
]

# Route 1: The root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the DevOps Task API!"}

# Route 2: Get all tasks
@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks_db}

@app.get("/health")
def health_check():
    return {"status": "healthy"}