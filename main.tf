resource "aws_ecs_service" "service" {
  name            = "${var.name}"
  task_definition = "${var.task_definition}"
  cluster         = "${var.cluster}"
  desired_count   = "${var.desired_count}"

	deployment_minimum_healthy_percent = "${var.deployment_minimum_healthy_percent}"
	deployment_maximum_percent         = "${var.deployment_maximum_percent}"

  placement_strategy {
    type  = "spread"
    field = "attribute:ecs.availability-zone"
  }

  placement_strategy {
    type  = "spread"
    field = "instanceId"
  }
}
