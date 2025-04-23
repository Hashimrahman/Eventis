from pydantic import BaseModel, EmailStr
from typing import Optional

class RegisterRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    confirm_password: str
    phone: str
    role: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str
    confirm_password: str


class UserResponse(BaseModel):
    id: Optional[str]
    full_name: str
    email: EmailStr
    # hashed_password: str
    phone: str = None
    role: str = "user"
    email_verified: bool = False
    is_active: bool
    is_admin: bool = False
    
    class Config:
        orm_mode = True