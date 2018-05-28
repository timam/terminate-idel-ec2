# Reading contents of history
file_handle = open('history.txt', "r")
raw_list = file_handle.readlines()
file_handle.close()

# Manipulating usage list
cpu_usage_str_list = [item.replace('\n', '') for item in raw_list]
cpu_usage_list = list(map(float,cpu_usage_str_list))

# Checking, if cpu is idle or not
if len(cpu_usage_list) < 15:
    print("Not enough Data")

else:
    if all(i < 20.0 for i in cpu_usage_list):
        print("Idle CPU")
    else:
        print("CPU is in use")