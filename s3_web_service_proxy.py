#!/usr/bin/env python
import json
import os
import urllib2


def handler(event, context):
    endpoint_url = os.environ['ENDPOINT_URL']
    event_json_string = json.dumps(event)

    web_service_response = proxy_event_to_web_service(event_json_string,
                                                      endpoint_url)

    response = {
        "statusCode": 200,
        "body": web_service_response
    }

    return response


class MethodRequest(urllib2.Request):
    def __init__(self, *args, **kwargs):
        if 'method' in kwargs:
            self._method = kwargs['method']
            del kwargs['method']
        else:
            self._method = None
        return urllib2.Request.__init__(self, *args, **kwargs)

    def get_method(self, *args, **kwargs):
        if self._method is not None:
            return self._method
        return urllib2.Request.get_method(self, *args, **kwargs)


def proxy_event_to_web_service(event, endpoint_url):
    request = MethodRequest(endpoint_url, method='PUT')
    request.add_header('Content-Type', 'application/json')

    response = urllib2.urlopen(request, event)

    return response.read()
