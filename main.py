from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("index.html")

@app.post("/sum")
async def sum(request: Request):
    num1 = await request.form['number1']
    num2 = await request.form['number2']
    return {'result': int(num1) + int(num2)}