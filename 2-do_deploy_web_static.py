#!/usr/bin/python3
'''
Fabric script
'''

from fabric.api import put, run, env
import os
env.hosts = ["100.27.12.93", "54.146.89.146"]


def do_deploy(archive_path):
    ''' an archive to the web servers'''
    if not os.path.isfile(archive_path):
        return False
    f = archive_path.split("/")[-1]
    no_ext = f.split(".")[0]
    path = "/data/web_static/releases/"
    if all([
        put(archive_path, "/tmp/{}".format(f)).failed,
        run("mkdir -p {}{}/".format(path, no_ext)).failed,
        run("tar -xzf /tmp/{} -C {}{}/".format(f, path, no_ext)).failed,
        run("rm /tmp/{}".format(f)).failed,
        run("mv -a /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(no_ext, no_ext)).failed,
        run("rm -rf {}{}/web_static".format(path, no_ext)).failed,
        run("rm -rf /data/web_static/current").failed,
        run("ln -s {}{}/ /data/web_static/current".format(path, no_ext)).failed
    ]):
        return False
    return True
