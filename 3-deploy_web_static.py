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
    f = archive_path.split("/")[-1]
    no_ext = f.split(".")[0]
    path = "/data/web_static/releases/"
    if all([
        put(archive_path, "/tmp/{}".format(f)).failed,
        run("mkdir -p {}{}/".format(path, no_ext)).failed,
        run("tar -xzf /tmp/{} -C {}{}/".format(f, path, no_ext)).failed,
        run("rm /tmp/{}".format(f)).failed,
        run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(
            no_ext, no_ext)).failed,
        run("rm -rf {}{}/web_static".format(path, no_ext)).failed,
        run("rm -rf /data/web_static/current").failed,
        run("ln -sf {}{}/ /data/web_static/current".format(
            path, no_ext)).failed,
        run("sudo chown -hR ubuntu:ubuntu /data/").failed
    ]):
        return False
    print("deployed!.")
    return True


def deploy():
    """Create and distribute an archive"""
    new_file = do_pack()
    if new_file is None:
        return False
    result = do_deploy(new_file)
    return result
