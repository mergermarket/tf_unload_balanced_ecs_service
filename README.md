AWS ECS Service terraform module
================================

[![Build Status](https://travis-ci.org/mergermarket/tf_unload_balanced_ecs_service.svg?branch=master)](https://travis-ci.org/mergermarket/tf_unload_balanced_ecs_service)

This module creates an ECS Service.

This ECS Service does not have associated Target Group and cannot be connected to AWS ALB (if you want to deploy ECS Service with Target Group, have a look at [tf_load_balanced_ecs_service](https://github.com/mergermarket/tf_load_balanced_ecs_service)).

Module Input Variables
----------------------

- `name` - (string) - **REQUIRED** - Name/name prefix to apply to the resources in the module
- `task_definition` - (string) - **REQUIRED** - The family and revision (family:revision) or full ARN of the task definition that you want to run in your service
- `cluster` - (string) - The name of the ECS cluster to deploy the service to
- `desired_count` - (string) - The number of instances of the task definition to place and keep running
- `deployment_minimum_healthy_percent` - (int) - The lower limit (as a percentage of the service's desiredCount) of the number of running tasks that must remain running and healthy in a service during a deployment
- `deployment_maximum_percent` - (int) - The upper limit (as a percentage of the service's desiredCount) of the number of running tasks that can be running in a service during a deployment

Usage
-----

```hcl
module "service" {
  source = "github.com/mergermarket/tf_unload_balanced_ecs_service"

  # required
  name            = "foobar"
  task_definition = "arn:aws:ecs:us-east-1:123456789012:task-definition/hello_world:8"
}
```

Outputs
-------

This plugin does not output anything
