#Normal Fast APi basic Structure
from fastapi import FastAPI

app = FastAPI()

# Home Route
@app.get("/")
def home():
    return {"message": "Hello, World! "}

# ABout Route
@app.get("/about")
def about():
    return {"message": "This is about page."}

#User Route
@app.get("/user")
def user():
    return {
        "users": ["Akshay", "Rohit"]
    }