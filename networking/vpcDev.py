import pulumi
import pulumi_aws as aws

TAGS_VPC_NAME="vpc-dev"
TAGS_IGW_NAME="igw-dev"
TAGS_SUBNET_PUBLIC_A="subnet-public-a-dev"
TAGS_SUBNET_PUBLIC_B="subnet-public-b-dev"
TAGS_SUBNET_PUBLIC_C="subnet-public-c-dev"
TAGS_SUBNET_PRIVATE_A="subnet-private-a-dev"
TAGS_SUBNET_PRIVATE_B="subnet-private-b-dev"
TAGS_SUBNET_PRIVATE_C="subnet-private-c-dev"
TAGS_RTB_PUBLIC_NAME="rtb-public-dev"
TAGS_RTB_PRIVATE_NAME="rtb-private-dev"


def vpcDev():
    infradev=aws.ec2.Vpc(
        "vpc-dev",
        cidr_block="10.0.0.0/16",
        instance_tenancy="default",
        enable_dns_hostnames=True,
        tags={
            "Name": TAGS_VPC_NAME
        }
    )

    igwdev=aws.ec2.InternetGateway(
        "igw-dev",
        vpc_id=infradev.id,
        tags={
            "Name": TAGS_IGW_NAME
        }
    )

    subnetPublicA=aws.ec2.Subnet(
        "subnet-public-A",
        vpc_id=infradev.id,
        availability_zone="us-east-1a",
        map_public_ip_on_launch=True,
        cidr_block="10.0.1.0/24",
        tags={
            "Name": TAGS_SUBNET_PUBLIC_A
        }
    )
    
    subnetPublicB=aws.ec2.Subnet(
        "subnet-public-B",
        vpc_id=infradev.id,
        availability_zone="us-east-1b",
        map_public_ip_on_launch=True,
        cidr_block="10.0.2.0/24",
        tags={
            "Name": TAGS_SUBNET_PUBLIC_B
        }
    )

    subnetPublicC=aws.ec2.Subnet(
        "subnet-public-C",
        vpc_id=infradev.id,
        availability_zone="us-east-1c",
        map_public_ip_on_launch=True,
        cidr_block="10.0.3.0/24",
        tags={
            "Name": TAGS_SUBNET_PUBLIC_C
        }
    )

    subnetPrivateA=aws.ec2.Subnet(
        "subnet-private-A",
        vpc_id=infradev.id,
        availability_zone="us-east-1a",
        cidr_block="10.0.11.0/24",
        tags={
            "Name": TAGS_SUBNET_PRIVATE_A
        }
    )
    
    subnetPrivateB=aws.ec2.Subnet(
        "subnet-private-B",
        vpc_id=infradev.id,
        availability_zone="us-east-1b",
        cidr_block="10.0.12.0/24",
        tags={
            "Name": TAGS_SUBNET_PRIVATE_B
        }
    )

    subnetPrivateC=aws.ec2.Subnet(
        "subnet-private-C",
        vpc_id=infradev.id,
        availability_zone="us-east-1c",
        cidr_block="10.0.13.0/24",
        tags={
            "Name": TAGS_SUBNET_PRIVATE_C
        }
    )

    routeTablePublic=aws.ec2.RouteTable(
        "rtb-public",
        vpc_id=infradev.id,
        routes=[
            aws.ec2.RouteTableRouteArgs(
                cidr_block="0.0.0.0/0",
                gateway_id=igwdev.id
            )
        ],
        tags={
            "Name": TAGS_RTB_PUBLIC_NAME
        }
    )

    routeTablePrivate=aws.ec2.RouteTable(
        "rtb-private",
        vpc_id=infradev.id,
        routes=[],
        tags={
            "Name": TAGS_RTB_PRIVATE_NAME
        }
    )

    routeTablePublicAssoc=aws.ec2.RouteTableAssociation(
        "rtb-public-asoc-A",
        route_table_id=routeTablePublic.id,
        subnet_id=subnetPublicA
    )

    routeTablePublicAssoc=aws.ec2.RouteTableAssociation(
        "rtb-public-asoc-B",
        route_table_id=routeTablePublic.id,
        subnet_id=subnetPublicB
    )

    routeTablePublicAssoc=aws.ec2.RouteTableAssociation(
        "rtb-public-asoc-C",
        route_table_id=routeTablePublic.id,
        subnet_id=subnetPublicC
    )

    routeTablePrivateAssoc=aws.ec2.RouteTableAssociation(
        "rtb-private-asoc-A",
        route_table_id=routeTablePrivate.id,
        subnet_id=subnetPrivateA
    )

    routeTablePrivateAssoc=aws.ec2.RouteTableAssociation(
        "rtb-private-asoc-B",
        route_table_id=routeTablePrivate.id,
        subnet_id=subnetPrivateB
    )

    routeTablePrivateAssoc=aws.ec2.RouteTableAssociation(
        "rtb-private-asoc-C",
        route_table_id=routeTablePrivate.id,
        subnet_id=subnetPrivateC
    )