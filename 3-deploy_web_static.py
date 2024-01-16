#!/usr/bin/python3
'''
Fabric script
'''

from fabric.api import put, run, env, local, runs_once
import os
import datetime
env.hosts = ["100.27.12.93", "54.146.89.146"]


def do_pack():
    '''
do_pack Funct generates  tgz archive
'''
    if not os.path.exists("versions"):
        os.mkdir("versions")
    now = datetime.datetime.now()
    t = now.strftime("%Y%m%d%H%M%S")
    out = f"versions/web_static_{t}.tgz"
    try:
        print("Packing web_static to {}".format(out))
        local("tar -cvzf {} web_static".format(out))
        size = os.stat(out).st_size
        print("web_static packed: {} -> {} Bytes".format(out, size))
    except Exception:
        out = None
    return out


def do_deploy(archive_path):
    ''' an archive to the web servers'''
    if not os.path.isfile(archive_path):
        return False
    try:
        f = archive_path.split("/")[-1]
        no_ext = f.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/{}".format(f))
        run("mkdir -p {}{}/".format(path, no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(f, path, no_ext))
        run("rm /tmp/{}".format(f))
        run("mv {0}{1}/web_static/ {0}{1}/".format(path, no_ext))
        run("rm -rf {}{}/web_static".format(path, no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}{}/ /data/web_static/current".format(
            path, no_ext))
        run("sudo chown -hR ubuntu:ubuntu /data/")
        print("deployed!.")
        return True
    except BaseException:
        return False


def deploy():
    """Create and distribute an archive"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
