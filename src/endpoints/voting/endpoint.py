from fastapi import FastAPI, Request

app = FastAPI(title="Rosa voting", version="0.0.1", summary="Rosa voting management")


@app.post("create")
async def create(request: Request):
    pass
