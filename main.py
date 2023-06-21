from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Welcome to the API"}


@app.get("/api")
def get_c(funct : str):
    if(funct == 'calculator'):
         return """
"""
# def perform_calculation():
    url = "http://localhost:8000/calculate"

    data = {
        "num1": "5",
        "operation": "+",
        "num2": "3"
    }

    response = requests.post(url, json=data)
    result = response.json()["result"]

    print("Result:", result)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

