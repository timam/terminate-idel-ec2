# Terminate Idle Ec2

EC2 are costly. If you create a lot of EC2 frequently, there is a chance that you will
forget to terminate when your task is completed. And you will end up paying bills to aws for nothing. 

This repository intends to stop you paying unwanted bills for EC2. 
By simply terminating your EC2 if it is idle for 15 minutes. 



Add the following line in /etc/rc.local.
```
exec /usr/bin/python3 /var/opt/monitor.py &
```

Edit crontab with "crontab -e" and add the following line.
```
* * * * * /var/opt/terminator.py
```


