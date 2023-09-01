import os
from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from src.components import run_all
from src.endpoint_resources import ResponseIndex
from src.settings import RAW_PATH, configure_logger

logger = configure_logger("RAG")

# Default values set up
model_name = "default"
version = "0.1.1"
origins = [
    "*",
]
description = """
Retrieval Augemented Generation API helps you to query PDF articles. 🚀

## Load PDFs to query them



"""
contact = {
    "name": "Roberto Galindo",
    "email": "roberto.galindo@wizeline.com",
}


logger.info("Starting app")
app = FastAPI(
    title="RAG API",
    description=description,
    contact=contact,
    version=version,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoints definition


@app.post("/upload_files", response_model=ResponseIndex, name="Upload files")
async def upload_files(
    project_name: str, question: str, files: List[UploadFile] = File(...)
):
    """Upload files and trigger indexing process"""
    # input = InputIndex(name=project_name, type="files")
    local_raw_dir = f"{RAW_PATH}/{project_name}"
    if not os.path.exists(local_raw_dir):
        os.mkdir(local_raw_dir)
    for file in files:
        with open(f"{local_raw_dir}/{file.filename}", "wb") as buffer:
            buffer.write(file.file.read())
            buffer.close()
    return ResponseIndex(response=run_all(human_query=question, path=local_raw_dir))
