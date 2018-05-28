import os

# Get CPU Usage
top = list(os.popen(''' top -b -d1 -n2 | grep -i "Cpu(s)" | tail -1  | awk '{ print $2 }' '''))
percentage = float((top[0]).replace("\n", ""))



