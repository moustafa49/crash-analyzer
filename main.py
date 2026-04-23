from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def analyze(data):
    if len(data) < 10:
        return {"result": "❗ محتاج داتا أكتر"}

    last18 = data[-18:]
    last5 = data[-5:]

    low = [x for x in last18 if x < 2]
    mid = [x for x in last18 if 2 <= x < 5]
    high = [x for x in last18 if x >= 5]

    result = ""

    # 🔥 موجة
    if len([x for x in last5 if x < 2]) >= 4:
        result = "🔥 موجة صعود جاية"

    elif len([x for x in last5 if x >= 5]) >= 3:
        result = "⚠️ خطر Crash"

    else:
        result = "🤔 السوق متقلب"

    # 🎯 رينج
    max_val = max(last18)

    if max_val >= 10:
        target = "🎯 5x - 7x"
    elif max_val >= 5:
        target = "🎯 3x - 5x"
    else:
        target = "🎯 1.5x - 3x"

    # 🧠 ثقة القرار
    confidence = round((len(low)/18)*100)

    return {
        "result": result,
        "target": target,
        "confidence": f"📊 ثقة: {confidence}%"
    }

@app.post("/analyze")
def run(data: list[float]):
    return analyze(data)
