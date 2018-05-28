import os


percentage = list(os.popen(''' top -b -d1 -n2 | grep -i "Cpu(s)" | tail -1  | cut -d ' ' -f2 '''))
temp = percentage[0]
var = temp[:-1]
print(var)


