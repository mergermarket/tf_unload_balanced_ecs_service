# fixture
module "service_raw" {
  source = "../.."

  # required
  name            = "${var.name}"
  task_definition = "${var.task_definition}"
}

module "service_with_custom_deployment_configuration" {
  source = "../.."

  # required
  name                               = "${var.name}"
  task_definition                    = "${var.task_definition}"
  deployment_minimum_healthy_percent = "${var.deployment_minimum_healthy_percent}"
  deployment_maximum_percent         = "${var.deployment_maximum_percent}"
}

module "service_with_custom_desired" {
  source = "../.."

  # required
  name            = "${var.name}"
  task_definition = "${var.task_definition}"
  desired_count   = "${var.desired_count}"
}

# configure provider to not try too hard talking to AWS API
provider "aws" {
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_get_ec2_platforms      = true
  skip_region_validation      = true
  skip_requesting_account_id  = true
  max_retries                 = 1
  access_key                  = "a"
  secret_key                  = "a"
  region                      = "eu-west-1"
}

# variables
variable "name" {}

variable "task_definition" {}

variable "desired_count" {
  default = ""
}

variable "deployment_minimum_healthy_percent" {
  default = ""
}

variable "deployment_maximum_percent" {
  default = ""
}
