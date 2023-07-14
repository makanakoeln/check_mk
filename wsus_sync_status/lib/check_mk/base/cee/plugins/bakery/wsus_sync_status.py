#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# def bake_wsus_sync_status(opsys, conf, conf_dir, plugins_dir):
#     if conf[0] == "activate":
#         shutil.copy2(cmk.utils.paths.local_agents_dir  + "/plugins/wsus_sync_status.ps1",
#                      plugins_dir + "/wsus_sync_status.ps1")
# 
#     #if conf == True:
#     #    conf = {}
# 
#         def write_wsus_sync_status_ini(path, port):
#             f = file(path, "w")
#             f.write("#define wsus port\n\n")
#             f.write("[connection]\n")
#             if port:
#                 f.write("port = %s\n" % port)
# 
# 
#         write_wsus_sync_status_ini(conf_dir + "/wsus_sync_status.ini", conf[1])
# 
# bakery_info["wsus_sync_status"] = {
#     "bake_function" : bake_wsus_sync_status,
#     "os"            : [ "windows" ],
# }

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

