from functools import wraps
from typing import List
from fastapi import Depends, FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from models import models
from database import engine
# from routers import master_data_router, login_router, bbki_router, bbki_download_csv, build_scenario_router
import logging
from routers import demo



models.Base.metadata.create_all(bind=engine)
middleware = [Middleware(CORSMiddleware, allow_origins=[
                         '*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])]

app = FastAPI(middleware=middleware)
app.include_router(demo.router)
# @AuthJWT.load_config
# def get_config():
#     return schema_common.Settings()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
