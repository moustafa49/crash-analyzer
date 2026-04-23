from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ حل المشكلة هنا
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def analyze(data):
    last = data[-20:]

    def classify(x):
        if x < 2:
            return "LOW"
        elif x < 5:
            return "MEDIUM"
        return "HIGH"

    classes = [classify(x) for x in last]

    if classes[-3:] == ["LOW", "LOW", "LOW"]:
        return {"result": "🔥 High"}

    if "HIGH" in classes[-2:]:
        return {"result": "⚠️ Low"}

    return {"result": "🤔 Wait"}

@app.get("/")
def home():
    return {"msg": "API شغال 🔥"}

@app.post("/analyze")
def run(data: list[float]):
    return analyze(data)
