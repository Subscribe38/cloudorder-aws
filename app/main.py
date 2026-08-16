from fastapi import FastAPI

app = FastAPI(title="CloudOrder API")


@app.get("/")
def home():
    return {"message": "CloudOrder API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
    