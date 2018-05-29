#!/usr/bin/python3

import signal
import boto3
from secrets import *
from time import sleep

client = boto3.client(
    'ec2',
    region_name=gimme_aws_region(),
    aws_access_key_id = gimme_aws_access_id(),
    aws_secret_access_key= gimme_aws_secret_access_key()
)

# Reading contents of history
file_handle = open('/var/opt/usage.log', "r")
raw_list = file_handle.readlines()
file_handle.close()

# Manipulating usage list
cpu_usage_str_list = [item.replace('\n', '') for item in raw_list]
cpu_usage_list = list(map(float,cpu_usage_str_list))

# Checking, if cpu is idle or not
if len(cpu_usage_list) < 15:
    print("Not enough Data")

else:
    if all(i < 20.0 for i in cpu_usage_list[-15:]):

        # Killing monitor.py
        monitor_pid = list(os.popen(''' ps -aux | grep -v grep | grep monitor.py | awk '{ print $2 }' '''))
        pid = (monitor_pid[0]).replace("\n", "")
        os.kill(int(pid), signal.SIGTERM)
        print("Killing pid" + pid)

        #Writing termination message
        with open("/var/opt/usage.log", "a") as file:
            file.write("CPU IDLE for last 15 mins, Terminating.....")

        sleep(60)

        #Terminating Instance
        response = client.terminate_instances(
            InstanceIds =  gimme_instence_id()
        )

    else:
        print("CPU is in use")