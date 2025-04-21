import os

from aws_cdk import App, DefaultStackSynthesizer, Environment

from aws_cdk_python.aws_cdk_python_stack import EC2InstanceStack

app = App()

EC2InstanceStack(
    app,
    "EC2InstanceStack",
    synthesizer=DefaultStackSynthesizer(
        cloud_formation_execution_role="arn:aws:iam::261179449440:LabRole/PrecreatedExecutionRole",
        deploy_role_arn="arn:aws:iam::261179449440:LabRole/PrecreatedDeployRole",
        file_assets_bucket_name="preexisting-assets-bucket",
        image_assets_repository_name="preexisting-ecr-repo",
        generate_bootstrap_version_rule=False,
    ),
    env=Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
    ),
)

app.synth()
