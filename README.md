# S3 web service proxy

[![Build Status](https://travis-ci.org/tomelliff/s3-web-service-proxy.svg?branch=master)](https://travis-ci.org/tomelliff/s3-web-service-proxy) [![Coverage Status](https://coveralls.io/repos/github/tomelliff/s3-web-service-proxy/badge.svg?branch=master)](https://coveralls.io/github/tomelliff/s3-web-service-proxy?branch=master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/07424b22b069429c93d0ae6c696a66bb)](https://www.codacy.com/app/tomelliff/s3-web-service-proxy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tomelliff/s3-web-service-proxy&amp;utm_campaign=Badge_Grade)

A basic Lambda function to proxy through the event to a PUT-able endpoint.

Specifically aimed at notifying an application of an S3 PUT event, making the process more event driven than just polling the S3 bucket.

TODO:
- Cloudformation to deploy things
  - Launch stack button
