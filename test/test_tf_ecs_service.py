import unittest
import os
import time
from subprocess import check_call, check_output

cwd = os.getcwd()


class TestTFECSService(unittest.TestCase):

    def setUp(self):
        check_call(['terraform', 'get', 'test/infra'])

    def test_create_ecs_service(self):
        # Given
        # ms since epoch
        name = 'test-' + str(int(time.time() * 1000))
        task_definition = (
            "arn:aws:ecs:us-east-1:123456789012:task-definition/hello_world:8"
        )

        # When
        output = check_output([
            'terraform',
            'plan',
            '-var', 'name={}'.format(name),
            '-var', 'task_definition={}'.format(task_definition),
            '-no-color',
            '-target=module.service_raw',
            'test/infra'
        ]).decode('utf-8')

        # Then
        assert """
+ module.service_raw.aws_ecs_service.service
    cluster:                             "default"
    deployment_maximum_percent:          "200"
    deployment_minimum_healthy_percent:  "100"
    desired_count:                       "3"
    name:                                "{name}"
    placement_strategy.#:                "2"
    placement_strategy.2093792364.field: "attribute:ecs.availability-zone"
    placement_strategy.2093792364.type:  "spread"
    placement_strategy.3946258308.field: "instanceId"
    placement_strategy.3946258308.type:  "spread"
    task_definition:                     "{task_definition}"
        """.format(
            name=name, task_definition=task_definition
        ).strip() in output

    def test_create_ecs_custom_deployment_configuration(self):
        # Given
        deployment_minimum_healthy_percent = 50
        deployment_maximum_percent = 100

        # When
        output = check_output([
            'terraform',
            'plan',
            '-var', 'name=foobar',
            '-var', 'task_definition=foobar:2',
            '-var', 'deployment_minimum_healthy_percent={}'.format(
                deployment_minimum_healthy_percent
            ),
            '-var', 'deployment_maximum_percent={}'.format(
                deployment_maximum_percent
            ),
            '-no-color',
            '-target=module.service_with_custom_deployment_configuration',
            'test/infra'
        ]).decode('utf-8')

        # Then
        assert """
+ module.service_with_custom_deployment_configuration.aws_ecs_service.service
    cluster:                             "default"
    deployment_maximum_percent:          "100"
    deployment_minimum_healthy_percent:  "50"
    desired_count:                       "3"
    name:                                "foobar"
    placement_strategy.#:                "2"
    placement_strategy.2093792364.field: "attribute:ecs.availability-zone"
    placement_strategy.2093792364.type:  "spread"
    placement_strategy.3946258308.field: "instanceId"
    placement_strategy.3946258308.type:  "spread"
    task_definition:                     "foobar:2"
        """.strip() in output

    def test_create_service_with_custom_desired(self):
        # Given
        desired_count = 16

        # When
        output = check_output([
            'terraform',
            'plan',
            '-var', 'name=foobar',
            '-var', 'task_definition=foobar:2',
            '-var', 'desired_count={}'.format(
                desired_count
            ),
            '-no-color',
            '-target=module.service_with_custom_desired',
            'test/infra'
        ]).decode('utf-8')

        # Then
        assert """
+ module.service_with_custom_desired.aws_ecs_service.service
    cluster:                             "default"
    deployment_maximum_percent:          "200"
    deployment_minimum_healthy_percent:  "100"
    desired_count:                       "{desired_count}"
    name:                                "foobar"
    placement_strategy.#:                "2"
    placement_strategy.2093792364.field: "attribute:ecs.availability-zone"
    placement_strategy.2093792364.type:  "spread"
    placement_strategy.3946258308.field: "instanceId"
    placement_strategy.3946258308.type:  "spread"
    task_definition:                     "foobar:2"
        """.format(desired_count=desired_count).strip() in output
