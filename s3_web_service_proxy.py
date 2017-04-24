#!/usr/bin/env python
import json
import os
import sys

# We need to package requests with the Lambda function so add it to path
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "vendored"))

import requests  # noqa: E402


def handler(event, context):
    endpoint_url = os.environ['ENDPOINT_URL']
    event_json_string = json.dumps(event)

    status_code, body = proxy_event_to_web_service(event_json_string,
                                                   endpoint_url)

    response = {
        "statusCode": status_code,
        "body": body
    }

    return response


def proxy_event_to_web_service(event, endpoint_url):
    r = requests.put(endpoint_url, data=event)

    r.raise_for_status()

    return r.status_code, r.json()
