from fastapi import APIRouter, Depends,HTTPException
from typing import List
from app.services.user_service import get_all_users
from app.core.security import isAdmin
from app.schemas.auth_schema import UserResponse

router = APIRouter(prefix='/api/v1/admin', tags=['admin'])

@router.get("/users-list", response_model=List[UserResponse])
async def get_all_users_route(_:dict = Depends(isAdmin)):
    return await get_all_users()
