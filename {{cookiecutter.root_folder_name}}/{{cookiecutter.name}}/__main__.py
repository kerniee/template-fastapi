from fastapi import FastAPI

from {{cookiecutter.name}} import __version__, __description__
from {{cookiecutter.name}}.endpoints import list_of_routers
from {{cookiecutter.name}}.config import DefaultSettings
from {{cookiecutter.name}}.utils import get_settings


def bind_routes(application: FastAPI, setting: DefaultSettings):
    for router in list_of_routers:
        application.include_router(router, prefix=setting.PATH_PREFIX)


def get_app() -> FastAPI:
    settings = get_settings()
    application = FastAPI(
        title="{{cookiecutter.name}}",
        description=__description__,
        version=__version__,
        debug=settings.DEBUG
    )
    bind_routes(application, settings)
    application.state.settings = settings
    return application


app = get_app()
