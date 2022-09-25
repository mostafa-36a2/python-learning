from fastapi import FastAPI

# python3 -m uvicorn x-basic:app -p 8000 --reload
# FastAPI Application.
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# python3 -m uvicorn x-basic:app --port 8001 --reload
# We can run many applications.
# https://stackoverflow.com/questions/69641363/how-to-run-fastapi-app-on-multiple-ports
another_app = FastAPI()


@another_app.get("/")
async def root():
    return {"message": "Good bye"}


# Run server:
# uvicorn main:app --reload
