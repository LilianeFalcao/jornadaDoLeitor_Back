from pydantic import BaseModel, ConfigDict, EmailStr


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

    model_config = ConfigDict(from_attributes=True)
