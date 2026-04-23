from fastapi import FastAPI

app = FastAPI()

def analyze(data):
    last = data[-20:]

    def classify(x):
        if x < 2:
            return "LOW"
        elif x < 5:
            return "MEDIUM"
        return "HIGH"

    classes = [classify(x) for x in last]

    if classes[-3:] == ["LOW","LOW","LOW"]:
        return {"result": "🔥 High قريب"}

    if "HIGH" in classes[-2:]:
        return {"result": "⚠️ Low جاي"}

    return {"result": "😐 العب على 2x"}

@app.get("/")
def home():
    return {"msg": "API شغال 🔥"}

@app.post("/analyze")
def run(data: list[float]):
    return analyze(data)
