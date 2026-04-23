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
        return {
            "result": "❌ محتاج بيانات أكتر",
            "target": "--",
            "confidence": "0%"
        }

    avg = sum(data[-10:]) / len(data[-10:])
    max_val = max(data)
    min_val = min(data)
    high_count = len([x for x in data if x > 2])

    if avg > 3 or max_val > 10:
        result = "🔥 دخول قوي"
        target = "5x → 7x"
        confidence = "80%"
        trend = "صاعد"
    elif avg > 2:
        result = "⚖️ متوسط"
        target = "2x → 5x"
        confidence = "60%"
        trend = "متوازن"
    else:
        result = "📉 ضعيف"
        target = "1x → 2x"
        confidence = "40%"
        trend = "هابط"

    return {
        "result": result,
        "target": target,
        "confidence": confidence,
        "trend": trend,
        "avg": round(avg, 2),
        "max": max_val,
        "min": min_val,
        "high_count": high_count
    }
