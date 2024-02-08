APP_NAME := cat_facts
VENV_DIR ?= "cat_facts-venv"
VENV := . ${VENV_DIR}/bin/activate
WEBAPP_SOURCE_DIR := cat_facts
SOURCE_DIRS := $(WEBAPP_SOURCE_DIR)

.PHONY: docker-up
docker-up:
	docker build -t cat_facts .
	docker run cat_facts

clean:
	rm -rf $(VENV_DIR)

venv:
	python -m venv $(VENV_DIR)
	$(VENV); pip install --upgrade pip
	$(VENV); pip install -r requirements.txt

lint: venv
	$(VENV); mypy $(SOURCE_DIRS)
	$(VENV); black --check $(SOURCE_DIRS)
	$(VENV); pylint $(SOURCE_DIRS)