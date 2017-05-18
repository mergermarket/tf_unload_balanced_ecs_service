# required
variable "name" {
  description = "Name/name prefix to apply to the resources in the module."
  type        = "string"
}

variable "task_definition" {
  description = "The family and revision (family:revision) or full ARN of the task definition that you want to run in your service."
  type        = "string"
}

# optional
variable "cluster" {
  description = "The name of the ECS cluster to deploy the service to."
  type        = "string"
  default     = "default"
}

variable "desired_count" {
  description = "The number of instances of the task definition to place and keep running."
  type        = "string"
  default     = "3"
}

variable "deployment_minimum_healthy_percent" {
  description = "The lower limit (as a percentage of the service's desiredCount) of the number of running tasks that must remain running and healthy in a service during a deployment"
  type        = "string"
  default     = 100
}

variable "deployment_maximum_percent" {
  description = "The upper limit (as a percentage of the service's desiredCount) of the number of running tasks that can be running in a service during a deployment"
  type        = "string"
  default     = 200
}
