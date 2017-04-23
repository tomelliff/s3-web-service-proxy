
import json
import os
import unittest

from mock import patch

import s3_web_service_proxy


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

    @patch('s3_web_service_proxy.proxy_event_to_web_service')
    def test_handler_passes_correct_args(self, mock_proxy):
        os.environ['ENDPOINT_URL'] = 'http://example.org'
        s3_web_service_proxy.handler(self.s3_put_event, 'context')
        mock_proxy.assert_called_once_with(json.dumps(self.s3_put_event),
                                           'http://example.org')

    @patch('s3_web_service_proxy.proxy_event_to_web_service',
           return_value='foo')
    def test_handler_returns_response(self, mock_proxy):
        self.assertEqual(s3_web_service_proxy.handler(self.s3_put_event,
                                                      'context'),
                         self.expected_response)


class TestHttpCall(unittest.TestCase):
    def test_proxy_posts_event(self):
        self.assertEquals(json.loads(
            s3_web_service_proxy.proxy_event_to_web_service(
                'event', 'http://httpbin.org/post'))['data'],
            'event')
