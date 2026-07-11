from fastapi import FastAPI

app = FastAPI(
    title="Project Mizan API",
    description="API untuk pencarian, verifikasi, dan eksplorasi hadis.",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Project Mizan API",
        "project": "Project Mizan",
        "version": "0.1.0",
        "status": "development"
    }