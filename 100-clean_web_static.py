#!/usr/bin/python3
'''
Fabric script
'''

import fabric.api

env.hosts = ["100.27.12.93", "54.146.89.146"]
env.user = "ubuntu"


def do_clean(number=0):
    ''' cleaning '''
    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1
    local(f'cd versions && ls -t | tail -n +{number} | xargs rm -rf')
    path = '/data/web_static/releases'
    run(f'cd {path} && ls -t | tail -n +{number} | xargs rm -rf')
