#!/usr/bin/env python3
# this script starts an API application using 
from fastapi import FastAPI, APIRouter

Banjo = FastAPI()


@Banjo.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(Banjo, host="0.0.0.0", port=8001, log_level="debug")
