import os
import shutil  # Just for copy file
import typing

from fastapi import FastAPI, File, Form, UploadFile
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
            <h2>Upload a file, to get filename:</h2>

            <form action="/upload" method="POST">
                <input type="file" id="myFile" name="filename"><br>
                <input type="submit">
            </form>

            <h2>Upload many files, to get files:</h2>
            <!-- https://html.form.guide/php-form/html5-input-type-file/ -->
            <form action="/mupload" method="POST" enctype="multipart/form-data">
                <input type="file" id="myFile" name="files" multiple><br>
                <input type="submit">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/upload")
async def upload(filename: str = Form()):
    print("file_name: ", filename)
    return {"message": filename}


@app.post("/mupload")
async def mupload(files: typing.List[UploadFile] = File(...)):
    file_names = {}
    for file in files:
        try:
            with open(os.path.join("uploads", file.filename), "wb") as buffer:
                shutil.copyfileobj(fsrc=file.file, fdst=buffer)
            file_names[file.filename] = "Success"
        except Exception as e:
            file_names[file.filename] = "Failed with exception: " + str(e)

    return {"files": file_names}
