from fastapi import FastAPI, Query
from datetime import datetime

app = FastAPI(title="PacmanService")

@app.get("/echo")
def echo(message: str = Query(..., description="Message to echo back")):
    """
    Echo endpoint:
    - Receives a string
    - Returns the same string + current timestamp
    """
    timestamp = datetime.utcnow().isoformat()
    return {
        "response": f"{message} | {timestamp}"
    }
