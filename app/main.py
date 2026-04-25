from fastapi import FastAPI
from pydantic import BaseModel
from app.service import run_prompt_playground

app = FastAPI()

class Request(BaseModel):
    input: str

@app.post("/run")
def run(req: Request):
    return run_prompt_playground(req.input)
