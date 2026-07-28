from fastapi import FastAPI

app = FastAPI(
    title = "ARES API",
    version = "1.0.0"
)

@app.get("/")
def root():
    return {
        "project": "ARES",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }