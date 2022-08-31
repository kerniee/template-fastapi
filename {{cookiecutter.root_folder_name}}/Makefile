PROJECT_NAME ?= {{cookiecutter.name}}
VERSION = $(shell python3 -c "import {{cookiecutter.name}}; print({{cookiecutter.name}}.__version__)" | tr '+' '-')
PROJECT_NAMESPACE ?= {{cookiecutter.namespace}}
REGISTRY_IMAGE ?= $(PROJECT_NAMESPACE)/$(PROJECT_NAME)

all:
	@echo "make env         - Create & setup development virtual environment"
	@echo "make run         - Run application using uvicorn"
	@echo "make lint		- Check code with pylama"
	@echo "make docker		- Build a docker image"
	@echo "make upload		- Upload docker image to the registry"
	@exit 0

env:
	rm -rf venv
	# создаем новое окружение
	python3.10 -m venv venv
	# обновляем pip
	venv/bin/pip install -U pip
	# устанавливаем основные + dev зависимости
	venv/bin/pip install -r requirements.txt
	venv/bin/pip install -r requirements.dev.txt

run:
	venv/bin/uvicorn {{cookiecutter.name}}.__main__:app --host 0.0.0.0 --port 8000 --reload

lint:
	venv/bin/pylama $(PROJECT_NAME)

format:
	venv/bin/isort $(PROJECT_NAME)
	venv/bin/black $(PROJECT_NAME)

docker:
	docker build -t $(PROJECT_NAME):$(VERSION) .

upload: docker
	docker tag $(PROJECT_NAME):$(VERSION) $(REGISTRY_IMAGE):$(VERSION)
	docker tag $(PROJECT_NAME):$(VERSION) $(REGISTRY_IMAGE):latest
	docker push $(REGISTRY_IMAGE):$(VERSION)
	docker push $(REGISTRY_IMAGE):latest