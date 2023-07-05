# from src import app
from fastapi import FastAPI
from src.routes import router
from .db import populate_database
app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/health")
def get_health():
    return {"status": "OK", "message": "Server is running"}



if __name__ == "__main__":
    import uvicorn

    # Populate the database before starting the application
    populate_database()
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
