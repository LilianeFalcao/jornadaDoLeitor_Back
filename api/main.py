from fastapi import FastAPI
from api.routes.user_router import router as user_router
from api.routes.auth_router import auth_router

app = FastAPI(
    title="Jornada do Leitor - um progresso de leituras",
    description="API que disponibilizará os dados para os acompanhamentos de leitura",
    version="0.0.1",
)

app.include_router(user_router, prefix="/api", tags=["users"])
app.include_router(auth_router, prefix="/api", tags=["auth"])


@app.get("/")
def read_root():
    return {"msg", "API em FastAPI"}
