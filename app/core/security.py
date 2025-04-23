import os
from datetime import datetime, timedelta
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
# from app.core.config import settings
from app.models.user_model import UserModel
from app.db.database import get_user_collection
from dotenv import load_dotenv
from bson import ObjectId

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserModel:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid Token")
        users = get_user_collection()
        user_data = await users.find_one({"_id": ObjectId(user_id)})
        if not user_data:
            raise HTTPException(status_code=404, detail="User Not Found")
        
        user_data["id"] = str(user_data.pop("_id"))
        user_data.pop("reset_token", None)
        user_data.pop("reset_token_expiry", None)
        if "name" in user_data:
            user_data["full_name"] = user_data.pop("name")
        user_data.setdefault("verification_token", None)
        return UserModel(**user_data)
    except JWTError:
        raise HTTPException(status_code=401, detail= "Invalid Token")
    
    
async def isAdmin(current_user: UserModel = Depends(get_current_user)):
    if not getattr(current_user, "is_admin", False):
        raise HTTPException(status_code=403, detail="Access Denied")
    return current_user