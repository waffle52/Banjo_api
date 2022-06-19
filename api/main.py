#!/usr/bin/env python3
"""main.py
This script starts an API application using FastAPI to manage my server
"""
from api.models import temp_quotes
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
import json
import mysql.connector
from passlib.context import CryptContext
from pydantic import BaseModel
import random
import subprocess
import os
from typing import Optional


# TODO: Clean up code, comment code, Set up correct Security and Database Access(Spaceghost, pacman, users instead of .env,) etc...
# Test comment for git upload
# Set up unit tests. pycode style code.

# load the .env file
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# set up env
fake_users_db = {
    "Admin": {
        "username": os.getenv("USERNAME"),
        "full_name": "Kyle Campbell",
        "email": os.getenv("EMAIL"),
        "hashed_password": os.getenv("PASS"),
        "disabled": False,
    }
}

# BaseModel Class that holds access token and the type of token.
class Token(BaseModel):
    access_token: str
    token_type: str

# ...
class TokenData(BaseModel):
    username: Optional[str] = None

# ...
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

# ...
class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Create APP Instance
Banjo = FastAPI()


"""
# ...
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# ...
def get_password_hash(password):
    return pwd_context.hash(password)

# ...
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

# ...
def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# ...
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# ...
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# ...
async def get_current_active_user(current_user:
                                  User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# ...
@Banjo.post("/api/token", response_model=Token)
async def login_for_access_token(form_data:
                                 OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username,
                             form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# ...
@Banjo.get("/api/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

# ...
@Banjo.get("/api/users/me/items/")
async def read_own_items(current_user:
                         User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
"""

# Path to turn ON or OFF Desktop Server.
@Banjo.get("/api/PC_START/{signal}")
async def send_signal(signal: str):
    list_files = subprocess.run(["python3", "/home/ubuntu/pc_start/send_signal.py",
                                 "{}".format(signal)])
    return ("Activated")

# Path to check if server is online, use for remote alerts.
@Banjo.get("/api/Online")
async def status():
    return ("Status: Online")
