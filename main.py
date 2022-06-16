import uvicorn
from fastapi import FastAPI
from typing import Optional
from action import Action



app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=80)