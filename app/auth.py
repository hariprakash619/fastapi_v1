from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.utils import create_access_token, verify_password, hash_password
from app.schemas import BookResponse
from datetime import timedelta

auth_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

user_db = {
    "user1": {
        "username": "user1",
        "password": hash_password("password")
    }
}
@auth_router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=timedelta(hours=1))
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    return {"username": "user1"} #fetch user from token hardcodeded for now

