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


def proxy_event_to_web_service(event, endpoint_url):
    request = urllib2.Request(endpoint_url)
    request.add_header('Content-Type', 'application/json')

    response = urllib2.urlopen(request, event)

    return response.read()
