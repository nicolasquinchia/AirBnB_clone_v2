#!/usr/bin/python3
"""meeeh
"""

from fabric.operations import local, run, put, env
import os
from datetime import datetime


env.hosts = ['34.75.178.156', '35.231.231.185']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    blahhh
    """

    if not os.path.exists(archive_path):
        return False

    name = archive_path.split('/')[-1]

    untar = "/data/web_static/releases/{}".format(name.replace('.tgz', ''))

    put(archive_path, '/tmp')
    run('mkdir -p ' + untar)
    run('tar -xzf /tmp/{} -C {}'.format(name, untar))
    run('rm /tmp/{}'.format(name))
    run("mv {}/web_static/* {}".format(untar, untar))
    run("rm -rf {}/web_static".format(untar))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(untar))
