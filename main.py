from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def analyze(data):
    if len(data) < 5:
        return {
            "result": "❗ محتاج داتا أكتر",
            "target": "-",
            "confidence": "-"
        }

    last = data[-10:]
    avg = sum(last) / len(last)

    high = len([x for x in last if x > 2])

    if avg > 3 and high >= 6:
        return {
            "result": "🔥 دخول قوي",
            "target": "5x → 7x",
            "confidence": "75%"
        }

    elif avg > 2:
        return {
            "result": "⚖️ متوسط",
            "target": "2x → 5x",
            "confidence": "60%"
        }

    else:
        return {
            "result": "📉 ضعيف",
            "target": "1x → 2x",
            "confidence": "40%"
        }

@app.post("/api/analyze")
def run(data: List[float]):
    return analyze(data)

@app.get("/")
def home():
    return {"msg": "API شغال 🔥"}
