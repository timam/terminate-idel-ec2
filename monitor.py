#!/usr/bin/python3

import os
from time import sleep

while True:
    # Get CPU Usage
    top = list(os.popen(''' top -b -d1 -n2 | grep -i "Cpu(s)" | tail -1  | awk '{ print $2 }' '''))
    percentage = (top[0]).replace("\n", "")

    # Write percentage in a history file
    with open("/var/opt/usage.txt", "a") as file:
        file.write(percentage + "\n")

    sleep(60)
