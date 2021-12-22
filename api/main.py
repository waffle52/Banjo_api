#!/usr/bin/env python3
"""main.py
This script starts an API application using FastAPI to manage my server
"""
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

# Create app instance
Banjo = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@Banjo.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
