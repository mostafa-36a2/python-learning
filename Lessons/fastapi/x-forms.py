# https://fastapi.tiangolo.com/tutorial/request-forms/
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <html>
        <head></head>
        <body>
            <form method="POST" action="/login">
                Username: <input type="email" name="username"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit" name="submit" value="Submit" />
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username, "password": password}
