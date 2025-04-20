"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws


# 1. Creamos grupo de seguridad
security_group = aws.ec2.SecurityGroup(
    "web-sg",
    description="Permitir SSH y HTTP",
    ingress=[
        {"protocol": "tcp", "from_port": 22, "to_port": 22, "cidr_blocks": ["0.0.0.0/0"]},
        {"protocol": "tcp", "from_port": 80, "to_port": 80, "cidr_blocks": ["0.0.0.0/0"]}
    ],
    egress=[{"protocol": "-1", "from_port": 0, "to_port": 0, "cidr_blocks": ["0.0.0.0/0"]}]
)

# 2. Creamos instancia
instance = aws.ec2.Instance(
    "MV-MVD-Pulumi",
    instance_type="t3.micro",
    ami="ami-0aa28dab1f2852040",
    key_name="vockey",
    vpc_security_group_ids=[security_group.id],
    root_block_device=aws.ec2.InstanceRootBlockDeviceArgs(
        volume_size=20
    ),
    tags={"Name": "MV-MVD-Pulumi"},
    opts=pulumi.ResourceOptions(
        depends_on=[security_group]
    )
)

# 3. Exportamos
pulumi.export("public_ip", instance.public_ip)