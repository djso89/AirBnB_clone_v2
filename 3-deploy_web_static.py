#!/usr/bin/python3
import os.path
from fabric.api import *
from fabric.contrib import files
from datetime import datetime


env.user = "ubuntu"
env.hosts = ['35.227.80.39', '18.215.169.130', '3.84.213.144']


def do_pack():
    """ store the path of the created archive"""

    if not os.path.exists('versions'):
        local('mkdir -p versions')
    else:
        pass
    format_time = datetime.now().strftime("%Y%m%d%H%M%S")
    stored_in_path = 'versions/web_static_{}.tgz'.format(format_time)
    result = local('tar cvfz {} web_static'.format(stored_in_path))

    if result.failed:
        return None
    else:
        return stored_in_path


def do_deploy(archive_path):
    """
    Transfers archive to the path
    """

    if not os.path.isfile(archive_path):
        return False

    base_name = os.path.basename(archive_path)
    r, ext = os.path.splitext(base_name)
    tkn = '/data/web_static/releases/{}'.format(r)

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(tkn))
        run("sudo tar -xzf /tmp/{} -C {}/".format(base_name, tkn))
        run("sudo rm /tmp/{}".format(b_name))
        run("sudo mv {}/web_static/* {}/".format(tkn, tkn))
        run("sudo rm -rf {}/web_static".format(tkn))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(tkn))
        print('New version uploaded!')
    except:
        return False
    else:
        return True


def deploy():
    """Creates and distributes an archive to web servers"""
    archive = do_pack()
    if archive is None:
        return False
    value = do_deploy(archive)
    return value
