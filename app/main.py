from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello CI Pipeline"}


@app.get("/health")
def health():
    return {"status": "ok"}