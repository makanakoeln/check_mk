#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from pathlib import Path
from typing import Any, Dict

from .bakery_api.v1 import FileGenerator, OS, Plugin, PluginConfig, register

def _get_wsus_sync_status_lines(port):
    yield "# define wsus port"
    yield "[connection]"
    if port:
        yield "port = %s" % port

def get_wsus_sync_status_files(conf: Dict[str, Any]) -> FileGenerator:
    yield Plugin(base_os=OS.WINDOWS,
                 source=Path("wsus_sync_status.ps1"))
    yield PluginConfig(base_os=OS.WINDOWS,
                 lines=list(_get_wsus_sync_status_lines(conf[1])),
                 target=Path("wsus_sync_status.ini"))

register.bakery_plugin(
    name="wsus_sync_status",
    files_function=get_wsus_sync_status_files,
)

