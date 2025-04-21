#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk_python.aws_cdk_python_stack import EC2InstanceStack

app = cdk.App()

EC2InstanceStack(
    app,
    "EC2InstanceStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
    ),
)

app.synth()
