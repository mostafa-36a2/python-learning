# https://stackoverflow.com/questions/65296604/how-to-return-a-htmlresponse-with-fastapi
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# python3 -m uvicorn x-basic:app -p 8000 --reload
# FastAPI Application.
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
