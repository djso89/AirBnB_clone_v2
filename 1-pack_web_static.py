#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of the
# web_static folder of your AirBnB Clone repo, using the function do_pack
from datetime import datetime
from fabric.api import local


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
