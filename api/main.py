from fastapi import FastAPI
from api.routes.user_router import user_router
from api.routes.auth_router import auth_router
from api.routes.reading_router import readings_router
from api.routes.manga_router import mangas_router

app = FastAPI(
    title="Jornada do Leitor - um progresso de leituras",
    description="API que disponibilizará os dados para os acompanhamentos de leitura",
    version="0.0.1",
)

app.include_router(user_router, prefix="/api", tags=["users"])
app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(readings_router, prefix="/api", tags=["readings"])
app.include_router(mangas_router, prefix="/api", tags=["mangas"])


@app.get("/")
def read_root():
    return {"msg", "API em FastAPI"}
