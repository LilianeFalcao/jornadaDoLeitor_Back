from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    nickname: str
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: str
    email: EmailStr


class UserResponse(BaseModel):
    id: str
    nickname: str
    email: EmailStr

    class Config:
        from_attibutes = True
