SOURCES=s3_web_service_proxy.py
DEPENDENCIES=requirements.txt
VENDORED_FOLDER=vendored
PACKAGE_NAME=s3-web-service-proxy.zip

.PHONY: all
all: build

$(VENDORED_FOLDER): $(DEPENDENCIES)
	pip install -r $(DEPENDENCIES) -t $(VENDORED_FOLDER)

$(PACKAGE_NAME): $(SOURCES) $(VENDORED_FOLDER)
	zip -r $(PACKAGE_NAME) $(SOURCES) $(VENDORED_FOLDER)

.PHONY: build
build: $(PACKAGE_NAME)

.PHONY: test
test: lint unit

.PHONY: lint
lint:
	flake8 --exclude .git,env,vendored

.PHONY: unit
unit:
	python -m unittest discover

.PHONY: clean
clean:
	rm s3-web-service-proxy.zip
	rm -rf vendored
