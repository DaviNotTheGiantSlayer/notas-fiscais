from fastapi import FastAPI
import sheetWriter


app = FastAPI()


@app.post("/{url}")
def read_root(url: str):
    sheetWriter.writeToSheet(url);