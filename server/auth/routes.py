import os
from fastapi import FastAPI, APIRouter, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from dotenv import load_dotenv
from auth.models import SignupRequest
from auth.hashing import hash_password, verify_password
from config.db import users_collection


router = APIRouter()
security = HTTPBasic()


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    '''
    Authenticate user using HTTP Basic Auth
     - Check if username exists
     - Verify password
    '''
    user = users_collection.find_one({"username":credentials.username})

    if not user: 
        raise HTTPException(status_code=401, detail="Username not found") 
    
    if not verify_password(credentials.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    return {"username":credentials.username, "role":user["role"]}



@router.post("/signup")
def signup(req: SignupRequest):
    '''
    Signup a new user
     - Check if username already exists
     - Hash password and store user details in DB
    '''
    existing_user = users_collection.find_one({"username": req.username})

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    user_data = {
        "username": req.username,
        "password": hash_password(req.password),
        "role": req.role
    }
    try:
        result = users_collection.insert_one(user_data)
        if result.acknowledged == True:
            return {"message": "User created successfully"}
    except Exception as e:
        print("\n\n\nDatabase error:", e, "\n\n\n")
        raise HTTPException(status_code=500, detail="Failed to create user")




@router.post("/login")
def login(user=Depends(authenticate)):
    '''
    Login a user
     - Verify username and password
    '''
    return {"message": f"Welcome {user['username']}!", "role": user["role"]}


