import pathlib
import shutil

import uvicorn

from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse

app = FastAPI()


@app.post("/")
async def upload_file(file: UploadFile):
    with open(file.filename, "wb") as fh:
        shutil.copyfileobj(file.file, fh)


@app.get("/", response_class=FileResponse)
async def find_file(file_name: str):
    return file_name


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
