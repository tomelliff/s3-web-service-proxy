###################################################################################################

resource "aws_lambda_function" "s3_web_service_proxy_lambda" {
  filename         = "${var.lambda_function_package_path}"
  function_name    = "${var.function_prefix}-${var.integration_name}"
  description      = "${var.lambda_description}"
  runtime          = "python2.7"
  role             = "${aws_iam_role.lambda_role.arn}"
  handler          = "s3_web_service_proxy.handler"
  source_code_hash = "${base64sha256(file("${var.lambda_function_package_path}"))}"
  timeout          = 10

  vpc_config {
    subnet_ids         = "${var.lambda_vpc_subnet_ids}"
    security_group_ids = "${var.lambda_vpc_security_group_ids}"
  }

  environment {
    variables = {
      WEB_SERVICE_ENDPOINT = "${var.web_service_endpoint}"
    }
  }
}

###################################################################################################
