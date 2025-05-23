import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process(request:Request,call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
@app.get("/item")
async def all_items():
    return {"foo":"bar"}