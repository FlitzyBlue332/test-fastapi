from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"18220031": "Muhammad Raihan Aulia"}