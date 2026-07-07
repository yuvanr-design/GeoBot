from fastapi import FastAPI

app = FastAPI(
    title="GeoBot API",
    description="AI Geography Chatbot",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "running",
        "project": "GeoBot",
        "message": "Welcome to GeoBot API 🚀"
    }