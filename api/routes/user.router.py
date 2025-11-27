from fastapi import APIRouter
from api.schemas.user_schemas import UserCreate
router = APIRouter()

@router.post("/users")
async def create_user(
    user: UserCreate,
    factory: 
):
    