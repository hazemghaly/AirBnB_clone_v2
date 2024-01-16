#!/usr/bin/python3
'''
Fabric script
'''

import fabric.api
import os


env.hosts = ["100.27.12.93", "54.146.89.146"]
env.user = "ubuntu"


def do_clean(number=0):
    ''' 
    cleaning
'''
    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
