from typing import Optional

from pydantic import BaseModel


class UserRequest(BaseModel):
    name: str
    weight: float
    description: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    name: str
    weight: float
    description: Optional[str] = None

    class Config():
        orm_mode = True
