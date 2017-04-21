###################################################################################################

resource "aws_s3_bucket" "event_bucket" {
  bucket = "${var.function_prefix}-${var.integration_name}-${data.aws_caller_identity.current.account_id}"

  tags {
    Name        = "${var.function_prefix}-${var.integration_name}-${data.aws_caller_identity.current.account_id}"
    Integration = "${var.integration_name}"
  }
}

###################################################################################################

resource "aws_lambda_permission" "allow_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.s3_web_service_proxy_lambda.arn}"
  principal     = "s3.amazonaws.com"
  source_arn    = "${aws_s3_bucket.event_bucket.arn}"
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = "${aws_s3_bucket.event_bucket.id}"

  lambda_function {
    lambda_function_arn = "${aws_lambda_function.s3_web_service_proxy_lambda.arn}"
    events              = ["s3:ObjectCreated:*"]
  }
}

###################################################################################################
