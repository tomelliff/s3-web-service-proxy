
import json
import os
import unittest

from mock import patch
import requests

import s3_web_service_proxy


@patch('s3_web_service_proxy.proxy_event_to_web_service',
       return_value=(200, 'foo'))
class TestHandler(unittest.TestCase):
    s3_put_event = json.loads("""{
  "Records": [
    {
      "eventVersion": "2.0",
      "eventTime": "1970-01-01T00:00:00.000Z",
      "requestParameters": {
        "sourceIPAddress": "127.0.0.1"
      },
      "s3": {
        "configurationId": "testConfigRule",
        "object": {
          "eTag": "0123456789abcdef0123456789abcdef",
          "sequencer": "0A1B2C3D4E5F678901",
          "key": "HappyFace.jpg",
          "size": 1024
        },
        "bucket": {
          "arn": "arn:aws:s3:::mybucket",
          "name": "sourcebucket",
          "ownerIdentity": {
            "principalId": "EXAMPLE"
          }
        },
        "s3SchemaVersion": "1.0"
      },
      "responseElements": {
        "x-amz-id-2": "EXAMPLE123/lambdaisawesome/mnopqrstuvwxyzABCDEFGH",
        "x-amz-request-id": "EXAMPLE123456789"
      },
      "awsRegion": "us-east-1",
      "eventName": "ObjectCreated:Put",
      "userIdentity": {
        "principalId": "EXAMPLE"
      },
      "eventSource": "aws:s3"
    }
  ]
}""")

    expected_response = {'statusCode': 200,
                         'body': 'foo'}

    def test_handler_passes_correct_args(self, mock_proxy):
        os.environ['ENDPOINT_URL'] = 'http://example.org'
        s3_web_service_proxy.handler(self.s3_put_event, 'context')
        mock_proxy.assert_called_once_with(json.dumps(self.s3_put_event),
                                           'http://example.org')

    def test_handler_returns_response(self, mock_proxy):
        self.assertEqual(s3_web_service_proxy.handler(self.s3_put_event,
                                                      'context'),
                         self.expected_response)


class TestHttpCall(unittest.TestCase):
    def test_proxy_puts_event(self):
        self.assertEquals(s3_web_service_proxy.proxy_event_to_web_service(
                            'event', 'http://httpbin.org/put')[0],
                          200)
        self.assertEquals(s3_web_service_proxy.proxy_event_to_web_service(
                            'event', 'http://httpbin.org/put')[1]['data'],
                          'event')

    def test_bad_status_is_raised(self):
        with self.assertRaises(requests.exceptions.HTTPError) as context:
            s3_web_service_proxy.proxy_event_to_web_service(
                'event', 'http://httpbin.org/status/500')

        self.assertTrue('INTERNAL SERVER ERROR' in str(context.exception))
