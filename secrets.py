import os

def gimme_instence_id():
    id = os.popen(''' wget -q -O - http://169.254.169.254/latest/meta-data/instance-id ''')
    return list(id)

def gimme_aws_region():
    return '-----------'

def gimme_aws_access_id():
    return '------------------'

def gimme_aws_secret_access_key():
    return '------------------------------------'
