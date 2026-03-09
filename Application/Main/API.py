from fastapi import FastAPI, Form
from pydantic import BaseModel
import os
from datetime import datetime, timedelta
import jwt


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

#User token
def create_token(username: str):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() +timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY , algorithm=ALGORITHM)
    return token

app = FastAPI()
class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

#API for register
@app.post("/register")
def register_user(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
    ):
    return {
        "status": "success","message": "User registered successfully"
    }

