from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(Exception)
async def exception_handler(request: Request, exception: Exception) -> Response:
    return JSONResponse({"detail": ", ".join(map(str, exception.args))}, 400)
