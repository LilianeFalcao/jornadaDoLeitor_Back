from fastapi import APIRouter, Depends, HTTPException
from api.schemas.user_schemas import UserCreate, UserResponse
from core.factories.use_case_factory import UseCaseFactory
from api.dependencies import get_use_case_factory, get_current_user
from core.domain.entity import User

user_router = APIRouter()


@user_router.post("/users")
async def create_user(
    user: UserCreate, factory: UseCaseFactory = Depends(get_use_case_factory)
):
    try:
        register_user_use_case = factory.create_register_user()
        created_user = await register_user_use_case.execute(
            nickname=user.nickname, email=user.email, password=user.password
        )
        return UserResponse(
            id=created_user.id,
            nickname=created_user.nickname.value,
            email=created_user.email.value,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.get("/me", response_model=UserResponse)
async def read_user_me(current_user: User = Depends(get_current_user)):
    return UserResponse(
        id=current_user.id,
        nickname=current_user.nickname.value,
        email=current_user.email.value,
    )
