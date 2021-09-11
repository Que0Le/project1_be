from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.api.errors.http_error import http_error_handler
from app.api.errors.validation_error import http422_error_handler
from app.api.routes.api import router as api_router
from app.core.config import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from app.core.events import create_start_app_handler, create_stop_app_handler

""" Static files """
from fastapi.staticfiles import StaticFiles
# periodic task
from fastapi_utils.tasks import repeat_every
from app.core.config import settings

def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    # TODO: restrict origin https://fastapi.tiangolo.com/tutorial/cors/
    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix=API_PREFIX)
    application.mount("/static", StaticFiles(directory="static"), name="static")
    
    return application


app = get_application()

@app.on_event("startup")
@repeat_every(seconds=30*60, wait_first=True)
def refresh_token():
    if settings.account:
        settings.account.connection.refresh_token()
        print("refreshing token: " + str(settings.account.get_current_user))