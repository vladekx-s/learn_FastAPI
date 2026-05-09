from fastapi import FastAPI
from other_api import route as rt
import uvicorn
from contextlib import asynccontextmanager
from core.models import Base, db_helper_obj

@asynccontextmanager
async def function(app: FastAPI):
    async with db_helper_obj.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=function)
app.include_router(rt)

# Отдельный эндпоинт
@app.get("/api")
def root():
    return ":)"

if __name__ == "__main__":
    uvicorn.run("main:app")