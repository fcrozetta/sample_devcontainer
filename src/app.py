from fastapi import FastAPI

app = FastAPI(title="Dev Container Example")


@app.get("/")
def get_root():
    return "IT WORKS"
