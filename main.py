from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# 🔥 حل مشكلة Failed to fetch
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 للتأكد إن السيرفر شغال
@app.get("/")
def home():
    return {"msg": "API شغال 🔥"}

# 🔹 التحليل
@app.post("/analyze")
def run(data: List[float]):

    # لو الداتا قليلة
    if len(data) < 5:
        return {
            "result": "❗ محتاج بيانات أكتر",
            "target": "-",
            "confidence": "ضعيف"
        }

    # ناخد آخر 18 جولة
    last = data[-18:]

    # تقسيم
    low = [x for x in last if x < 2]
    mid = [x for x in last if 2 <= x < 5]
    high = [x for x in last if x >= 5]

    # تحليل الاتجاه
    if len(low) >= len(mid) and len(low) >= len(high):
        prediction = "🔥 High جاي"
        target = "3x → 6x"
        confidence = "متوسط"
    elif len(mid) >= len(low) and len(mid) >= len(high):
        prediction = "⚖️ Medium"
        target = "2x → 4x"
        confidence = "متوسط"
    else:
        prediction = "⚠️ Low غالب"
        target = "1.1x → 2x"
        confidence = "ضعيف"

    # 🧠 موجة Low → انفجار
    if len(last) >= 3 and all(x < 2 for x in last[-3:]):
        prediction = "🚀 Bounce قوي"
        target = "5x → 10x"
        confidence = "عالي"

    # 🧠 لو فيه رقم عالي قريب
    if any(x > 10 for x in last[-5:]):
        prediction = "⚠️ بعد High غالباً Low"
        target = "1.1x → 2x"
        confidence = "عالي"

    return {
        "result": prediction,
        "target": target,
        "confidence": confidence
    }
