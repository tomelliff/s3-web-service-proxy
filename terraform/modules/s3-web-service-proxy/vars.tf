###################################################################################################

variable "integration_name" {}

variable "function_prefix" {
  default = "s3-web-service-proxy"
}

###################################################################################################

variable "lambda_function_package_path" {}

variable "lambda_description" {
  default = "Managed by Terraform"
}

variable "lambda_vpc_subnet_ids" {
  type = "list"
}

variable "lambda_vpc_security_group_ids" {
  type = "list"
}

###################################################################################################

variable "web_service_endpoint" {}

###################################################################################################
