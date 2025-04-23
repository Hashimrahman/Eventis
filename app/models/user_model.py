from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    id: Optional[str]
    full_name: str
    email: EmailStr
    hashed_password: str
    phone: str
    role: str
    email_verified: bool = False
    verification_token: Optional[str]
    is_active: bool = True
    is_admin: bool = False
    reset_token: Optional[str] = None
    reset_token_expiry: Optional[datetime] = None


