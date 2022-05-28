# Getter methods for API functions.
# PacManScoreTracker HTTP Methods, get score by rank
"""
@Banjo.get("/PacManScoreTracker/{pos}")
async def get_score(score, token: str = Depends(oauth2_scheme)):
    return {"item": pos}
"""
"""
@Banjo.get("/SpaceGhostQuotes/")
async def random_quote():
    # Gets a random quote from the MySQL database
    rdm = random.randint(0, len(temp_quotes.quotes) - 1)
    print("Test: {}".format(rdm))
    return (temp_quotes.quotes[rdm].read())
"""
"""
@Banjo.get("/SpaceGhostQuotes/{index}")
async def select_quote(index):
    # Import from models list of quotes and return quote from index via id
    print("Test: {}".format(temp_quotes.quotes[index].read()))
    return (quote_id)
"""
