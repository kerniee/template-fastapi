from os import environ

from {{cookiecutter.name}}.config.default import DefaultSettings


def get_settings():
    env = environ.get("ENV", "local")
    if env == "local":
        return DefaultSettings()
    # ...
    # space for other settings
    # ...
    return DefaultSettings()  # fallback to default
