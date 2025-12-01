from fastapi import APIRouter, Depends, HTTPException
from api.schemas.user_schemas import UserCreate, UserResponse
from core.factories.use_case_factory import UseCaseFactory
from api.dependencies import get_use_case_factory

router = APIRouter()


@router.post("/users")
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
