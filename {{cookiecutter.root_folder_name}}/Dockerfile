FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV MODULE_NAME={{cookiecutter.name}}.__main__

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#COPY ./prestart.sh /app/prestart.sh

ENV PYTHONPATH=/app/{{cookiecutter.name}}
COPY ./{{cookiecutter.name}} /app/{{cookiecutter.name}}