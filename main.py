from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

class NumberList(BaseModel):
    numbers: List[int]

@app.post("/oii/sort-and-analyze")
def analyze_numbers(data: NumberList):
    raw_list = data.numbers

    sorted_list = sorted(raw_list)
    maximum = max(raw_list) if raw_list else 0
    unique_count = len(set(raw_list))

    return {
        "sorted": sorted_list,
        "max": maximum,
        "unique_elements": unique_count,
        "count": len(raw_list)
    }
