#!/usr/bin/env python3
"""main.py
This script starts an API application using FastAPI to manage my server
"""
from fastapi import FastAPI, APIRouter, Depends
from fastapi.security import HTTPBearer

# Scheme for the Authorization header
token_auth_scheme = HTTPBearer()

# Create app instance
Banjo = FastAPI()


@Banjo.get("/api/public")
def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": ("Hello from a public endpoint! You don't need to be "
                "authenticated to see this.")
    }
    return (result)


@Banjo.get("/api/private")
def private(token: str = Depends(token_auth_scheme)):
    """A valid access token is required to access this route"""
    result = token.credentials
    return (result)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(Banjo, host="0.0.0.0", port=8001, log_level="debug")
