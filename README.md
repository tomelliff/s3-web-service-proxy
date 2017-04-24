# S3 web service proxy

[![Build Status](https://travis-ci.org/tomelliff/s3-web-service-proxy.svg?branch=master)](https://travis-ci.org/tomelliff/s3-web-service-proxy) [![Coverage Status](https://coveralls.io/repos/github/tomelliff/s3-web-service-proxy/badge.svg?branch=master)](https://coveralls.io/github/tomelliff/s3-web-service-proxy?branch=master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/07424b22b069429c93d0ae6c696a66bb)](https://www.codacy.com/app/tomelliff/s3-web-service-proxy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tomelliff/s3-web-service-proxy&amp;utm_campaign=Badge_Grade)

A basic Lambda function to proxy through the event to a PUT-able endpoint.

Specifically aimed at notifying an application of an S3 PUT event, making the process more event driven than just polling the S3 bucket.

## Requirements

* Python 2.7
* [pip](https://pypi.python.org/pypi/pip)
* [virtualenv](https://pypi.python.org/pypi/virtualenv)
* [boto3](http://boto3.readthedocs.io/en/latest/)

## Building it

### Build the Lambda zip with dependencies included
```sh
make build
```

## Deploying

### Manually
Simply upload the zip produced by the build step above to a Lambda function with the Python 2.7 run time and the handler set to `s3_web_service_proxy.handler`.

### Terraform
This repo provides a [Terraform module](https://github.com/tomelliff/s3-web-service-proxy/tree/master/terraform/modules/s3-web-service-proxy) that will deploy and configure the Lambda function and supporting infrastructure with minimal configuration.

It currently requires lists of subnet IDs and security group IDs as the expectation is that this Lambda function would spawn inside a VPC to proxy the request through to an application that doesn't publicly expose this API. That said, there's no real reason why this has to be the case so at some point these will become optional rather than required.

## Contributing

### Set up virtualenv
```sh
virtualenv env
. env/bin/activate
```

### Run the tests
```sh
make test
```


TODO:
- Terraform - make VPC configuration optional
- Cloudformation to deploy things
  - Launch stack button
