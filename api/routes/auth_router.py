from fastapi import APIRouter, Depends, HTTPException, status
from api.schemas.user_schemas import UserCreate, UserResponse
from core.factories.use_case_factory import UseCaseFactory
from api.dependencies import get_use_case_factory
from fastapi.security import OAuth2PasswordRequestForm

from core.security import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from datetime import timedelta


@router.post("/token")
async def login_for_acess_token(
    form_data: OAuth2PasswordRequestForm,
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    login_user_use_case: factory.create_login_user()
    user = await login_user_use_case.execute(
        email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
