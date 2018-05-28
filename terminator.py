#!/usr/bin/python3

import boto3
from secrets import *

client = boto3.client(
    'ec2',
    region_name=gimme_aws_region(),
    aws_access_key_id=gimme_aws_access_id(),
    aws_secret_access_key=gimme_aws_secret_access_key()
)
# Reading contents of history
file_handle = open('usage.txt', "r")
raw_list = file_handle.readlines()
file_handle.close()

# Manipulating usage list
cpu_usage_str_list = [item.replace('\n', '') for item in raw_list]
cpu_usage_list = list(map(float, cpu_usage_str_list))

# Checking, if cpu is idle or not
if len(cpu_usage_list) < 15:
    print("Not enough Data")

else:
    if all(i < 20.0 for i in cpu_usage_list[-15:]):
        print("Idle CPU")

        response = client.stop_instances(
            InstanceIds=gimme_instence_id()
        )


    else:
        print("CPU is in use")