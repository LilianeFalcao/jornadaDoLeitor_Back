from fastapi import FastAPI

app = FastAPI(
    title="Jornada do Leitor - um progresso de leituras",
    description="API que disponibilizará os dados para os acompanhamentos de leitura",
    version="0.0.1",
)


@app.get("/")
def read_root():
    return {"msg", "API em FastAPI"}
