from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

with open('athletes.txt', 'r') as fi:
    database = [name.strip() for name in fi]

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/athletes")
async def athlete():
    return {"result": database}

@app.get("/athletes/{athlete_id}")
async def athletes(athlete_id: int):
    if athlete_id > len(database):
        raise HTTPException(status_code=404, detail="Uh Oh!")
    return {"result": database[athlete_id]}
