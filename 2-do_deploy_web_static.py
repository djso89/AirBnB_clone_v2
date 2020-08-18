#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents
import os.path
from fabric.api import *
from fabric.contrib import files
from datetime import datetime


env.user = "ubuntu"
env.hosts = ['35.227.80.39', '18.215.169.130', '3.84.213.144']


def do_pack():
    """Generates a .tgz archive from web_static"""
    local('mkdir -p versions')

    format_time = datetime.now().strftime("%Y%m%d%H%M%S")
    stored_in_path = 'versions/web_static_{}.tgz'.format(format_time)

    result = local('tar cvfz {} web_static'.format(stored_in_path))

    if result.failed:
        return None
    else:
        return result


def do_deploy(archive_path):
    """ Transfers archive_path to web servers above
    """

    if not os.path.isfile(archive_path):
        return False

    b_name = os.path.basename(archive_path)
    r, ext = os.path.splitext(b_name)
    token = '/data/web_static/releases/{}'.format(r)

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(token))
        run("sudo tar -xzf /tmp/{} -C {}/".format(b_name, token))
        run("sudo rm /tmp/{}".format(b_name))
        run("sudo mv {}/web_static/* {}/".format(token, token))
        run("sudo rm -rf {}/web_static".format(token))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(token))
        print('New version uploaded!')
    except:
        return False
    else:
        return True
