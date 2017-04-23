SOURCES=s3_web_service_proxy.py
PACKAGE_NAME=s3-web-proxy.zip

all: build

$(PACKAGE_NAME): $(SOURCES)
	zip -9 $(PACKAGE_NAME) $(SOURCES)

build: test $(PACKAGE_NAME)

.PHONY: test
test: lint unit

.PHONY: lint
lint:
	flake8 --exclude env/

.PHONY: unit
unit:
	python -m unittest discover
