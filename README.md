# S3 web service proxy

A basic Lambda function to proxy through the event to a POSTable endpoint.

Specifically aimed at notifying an application of an S3 PUT event, making the process more event driven than just polling the S3 bucket.

TODO:
- Change to PUT to be more semantically correct (?)
- Cloudformation to deploy things
  - Launch stack button
