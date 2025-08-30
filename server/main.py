from fastapi import FastAPI
from auth.routes import router as auth_router
from docs.routes import router as docs_router
from chat.routes import router as chat_router

app = FastAPI(title="Baymax API", description="Authentication API for Baymax", version="1.0.0")

app.include_router(auth_router, tags=["auth"])
app.include_router(docs_router, tags=["docs"])
app.include_router(chat_router, tags=["chat"])

@app.get("/")
def root():
    return {
        "message": "Welcome to Baymax API", 
        "documentation": "/docs",
        "health": "/health",
        "endpoints": {
            "signup": "POST /signup",
            "login": "POST /login",
            "upload_docs": "POST /upload_docs",
            "chat": "POST /chat"
        }
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}

def main():
    print("Server is running...")

if __name__ == "__main__":
    main()


# Run with: uvicorn main:app --reload