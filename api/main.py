#!/usr/bin/env python3
# This script starts an API application using FastAPI to manage my server
from fastapi import FastAPI, APIRouter

Banjo = FastAPI()


# PacManScoreTracker HTTP Methods
@Banjo.get("/PacManScoreTracker/{score}")
async def take_score(score):
    return {"item": score}


# practice section.
# SpaceGhostQuotes HTTP Methods
@Banjo.get("/SpaceGhostQuotes/")
async def random_quote():
    # Gets a random quote from the MySQL database
    return ("test")


@Banjo.get("/SpaceGhostQuotes/{quote_id}")
async def select_quote(quote_id):
    # Import from models list of quotes and return quote from index via id
    return (quote_id)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(Banjo, host="0.0.0.0", port=8001, log_level="debug")
