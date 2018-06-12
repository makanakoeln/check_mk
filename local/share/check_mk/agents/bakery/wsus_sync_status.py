#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import cmk.defines as defines

subgroup_applications = _("Applications, Processes & Services")

register_check_parameters(
    subgroup_applications,
    "wsus_sync_status",
    _("Time since last WSUS sync"),
    Dictionary(
        elements = [
            ("wsus_sync",
                Tuple(
                    title = _("Specify time since last successful WSUS sync"),
                    elements = [
                        Age(title = _("Warning if older than")),
                        Age(title = _("Critical if older than"))
                               ]
                     ),
            ),
                  ]
              ),
    TextAscii(
        title = _("Service descriptions"),
        allow_empty = False),
    "dict"
)

