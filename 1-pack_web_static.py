#!/usr/bin/python3
"""Meh
"""

import tarfile
import os
from datetime import datetime

def do_pack():
    """COmpresses
    """
    filename = 'web_static' + datetime.now().strftime('%Y%M%D%H%M%S') + '.tgz'
    try:
        if not os.path.isdir('versions'):
            os.mkdir('versions')
        with tarfile.open('versions' + filename, 'w:gz') as tar:
            tar.add('web_static', arcname=os.path.basename('web_static'))
        return 'savedir' + filename
    except Exception:
        return None
