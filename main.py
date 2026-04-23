from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "API شغال 🔥"}

@app.post("/analyze")
def run(data: List[float]):

    if len(data) < 5:
        return {
            "result": "❗ محتاج بيانات أكتر",
            "target": "-",
            "confidence": "ضعيف"
        }

    last = data[-18:]  # آخر 18 زي اللعبة

    # تقسيم القيم
    low = [x for x in last if x < 2]
    mid = [x for x in last if 2 <= x < 5]
    high = [x for x in last if x >= 5]

    # متوسط
    avg = sum(last) / len(last)

    # تحليل بسيط ذكي
    if len(low) >= len(mid) and len(low) >= len(high):
        prediction = "🔥 High جاي"
        target = "3x → 6x"
        confidence = "متوسط"
    elif len(mid) >= len(low) and len(mid) >= len(high):
        prediction = "⚖️ Medium"
        target = "2x → 4x"
        confidence = "متوسط"
    else:
        prediction = "⚠️ خطر"
        target = "1.1x → 2x"
        confidence = "ضعيف"

    # لو فيه موجة Low متتالية
    if len(last) >= 3 and all(x < 2 for x in last[-3:]):
        prediction = "🚀 Bounce قوي"
        target = "5x → 10x"
        confidence = "عالي"

    # لو فيه رقم كبير قريب
    if any(x > 10 for x in last[-5:]):
        prediction = "⚠️ بعد High غالباً Low"
        target = "1.1x → 2x"
        confidence = "عالي"

    return {
        "result": prediction,
        "target": target,
        "confidence": confidence
    }
