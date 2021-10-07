# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import os
from biovis_media_extension.plugin import BasePlugin


class UpsetRPlugin(BasePlugin):
    """
    Upset plugin for biovis_media_extension.

    :Example:
    @upset-r()
    """
    plugin_name = 'upset-r'
    plugin_dir = os.path.dirname(os.path.abspath(__file__))
    is_server = True

    def __init__(self, *args, **kwargs):
        super(UpsetRPlugin, self).__init__(*args, **kwargs)

    def check_plugin_args(self, **kwargs):
        pass
