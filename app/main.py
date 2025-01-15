from fastapi import FastAPI
from app.database import Base, engine
from app.auth import auth_router
from app.crud import books_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Books API", description="CRUD API for managing books", version="1.0.0")

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(books_router, prefix="/books", tags=["Books"])

@app.get("/")
def root():
    return {"message": "Welcome to the Books API"}
