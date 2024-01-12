#!/usr/bin/python3
from fabric.api import local, runs_once
import os
import datetime

@runs_once
def do_pack():
    os.mkdir("versions")
    now = datetime.datetime.now()
    t = now.strftime("%Y%m%d%H%M%S")
    file = f"versions/web_static_{t}.tgz"
    try:
        print("Packing web_static to {}".format(out))
        local("tar -cvzf {} file".format(out))
        size = os.stat(out).st_size
        print("web_static packed: {} -> {} Bytes".format(out, size))
    except Exception:
        out = None
    return out
