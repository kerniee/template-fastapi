from {{cookiecutter.name}}.endpoints.health_check import router as some_router
from {{cookiecutter.name}}.endpoints.example import router as example_router

list_of_routers = (
    some_router,
    example_router,
)

__all__ = [
    "list_of_routers",
]
