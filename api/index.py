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

@app.get("/api")
def home():
    return {"msg": "API شغال 🔥"}

@app.post("/api/analyze")
def analyze(data: List[float]):
    if len(data) < 5:
        return {"result": "❗ محتاج داتا أكتر", "target": "-"}

    avg = sum(data[-10:]) / len(data[-10:])

    if avg > 3:
        return {"result": "🔥 دخول قوي", "target": "5x → 7x"}
    elif avg > 2:
        return {"result": "⚖️ متوسط", "target": "2x → 5x"}
    else:
        return {"result": "📉 ضعيف", "target": "1x → 2x"}
