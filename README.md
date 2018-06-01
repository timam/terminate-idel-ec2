#Terminate Idle Ec2


Add the following line in /etc/rc.local.
```
exec /usr/bin/python3 /var/opt/monitor.py &
```

Edit crontab with "crontab -e" and add the following line.
```
* * * * * /var/opt/terminator.py
```


