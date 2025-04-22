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
    email_verified: bool = True
    verification_token: Optional[str]
    is_active: bool = True
    reset_token: Optional[str] = None
    reset_token_expiry: Optional[datetime] = None
