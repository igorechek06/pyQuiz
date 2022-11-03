from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(Exception)
@app.exception_handler(HTTPException)
async def exception_handler(request: Request, exception: Exception) -> Response:
    if isinstance(exception, HTTPException):
        message = exception.detail
        status = exception.status_code
    else:
        message = ", ".join(map(str, exception.args))
        status = 400

    return JSONResponse({"message": message}, status)
