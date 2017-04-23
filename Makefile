SOURCES=s3_web_service_proxy.py
PACKAGE_NAME=s3-web-proxy.zip

all: build

$(PACKAGE_NAME): $(SOURCES)
	zip -9 $(PACKAGE_NAME) $(SOURCES)

build: $(PACKAGE_NAME)
