from fastapi import FastAPI

from iam_api.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": settings.APP_NAME,
    }