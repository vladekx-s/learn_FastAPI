from fastapi import *
from other_api import route as rt
import uvicorn

app = FastAPI()
app.include_router(rt)

# Отдельный эндпоинт
@app.get("/api")
def root():
    return ":)"

if __name__ == "__main__":
    uvicorn.run("main:app")