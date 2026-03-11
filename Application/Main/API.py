from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import os
from datetime import datetime, timedelta
import jwt
import bcrypt
from Application.MySQL.Database import SessionLocal
from Application.MySQL.Model import User

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

# User token
def create_token(user_id: int):
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(hours=1),
        }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


app = FastAPI()


# Valid API data
class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str


# API to record new register
@app.post("/register")
def register_user(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
    ):
    db = SessionLocal()

    # Check if email already exists
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        return RedirectResponse(
            url="http://localhost:8000/Registration.html?error=email_exists",
            status_code=302,
        )

    # Hash the password before saving it to the database
    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),  # Convert the password from string to bytes
        bcrypt.gensalt()  # Generate a random salt to make the hash stronger
    ).decode()  # Convert the hashed bytes -> string -> stored in the database

    # Create new user object
    new_user = User(
        username=username,
        email=email,
        password=hashed_password
        )

    # Save to DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_token(new_user.id)

    # After successful registration, redirect to Login page
    response = RedirectResponse(
        url="http://localhost:8000/Login.html",
        status_code=302,
        )

    response.set_cookie(
        key="token",        # Name of the cookie
        value=token,        # Value stored in the cookie (usually a JWT or session token)
        httponly=True,      # Makes the cookie inaccessible to JavaScript
        max_age=3600        # Lifetime of the cookie in seconds (here: 1 hour)
        )
    return response

@app.post("/login")
def login_user(
    username: str = Form(...),
    password: str = Form(...),
):
    db = SessionLocal()

    user = db.query(User).filter(User.username == username).first()
    if not user:
        return RedirectResponse(
            url="http://localhost:8000/Login.html?error=wrong_password",
            status_code=302,
        )

    # Compare user-input password and the one in database
    if not bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        return RedirectResponse(
            url="http://localhost:8000/Login.html?error=wrong_password",
            status_code=302,
        )

    token = create_token(user.id)

    # Return token via cookie and redirect to Todo dashboard
    response = RedirectResponse(
        url="http://localhost:8000/TodoDashboard.html",
        status_code=302,
        )
    
    response.set_cookie(
        key="token",        
        value=token,        
        httponly=True,      
        max_age=3600       
        )
    return response

