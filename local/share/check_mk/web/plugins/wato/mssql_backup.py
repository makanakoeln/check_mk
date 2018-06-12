#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import cmk.defines as defines

subgroup_applications = _("Applications, Processes & Services")

register_check_parameters(
    subgroup_applications,
    "mssql_backup",
    _("MSSQL Time since last Backup"),
    Dictionary(
        elements = [
            ("db",
                Tuple(
                    title = _("Specify time since last successful database backup"),
                    elements = [
                        Age(title = _("Warning if older than")),
                        Age(title = _("Critical if older than"))
                               ]
                     ),
            ),
            ("log",
                Tuple(
                    title = _("Specify time since last successful log backup"),
                    elements = [
                        Age(title = _("Warning if older than")),
                        Age(title = _("Critical if older than"))
                               ]
                     ),
            ),
            ("db_diff",
                Tuple(
                    title = _("Specify time since last successful database diff backup"),
                    elements = [
                        Age(title = _("Warning if older than")),
                        Age(title = _("Critical if older than"))
                               ]
                     ),
            ),
            ("file_or_group",
                Tuple(
                    title = _("Specify time since last successful file or filegroup backup"),
                    elements = [
                        Age(title = _("Warning if older than")),
                        Age(title = _("Critical if older than"))
                               ]
                     ),
            ),
            ("file_diff",
                Tuple(
                    title = _("Specify time since last successful file diff backup"),
                    elements = [
                        Age(title = _("Warning if older than")),
                        Age(title = _("Critical if older than"))
                               ]
                     ),
            ),
            ("partial_backup",
                Tuple(
                    title = _("Specify time since last successful partial backup"),
                    elements = [
                        Age(title = _("Warning if older than")),
                        Age(title = _("Critical if older than"))
                               ]
                     ),
            ),
            ("partial_diff",
                Tuple(
                    title = _("Specify time since last successful partial diff backup"),
                    elements = [
                        Age(title = _("Warning if older than")),
                        Age(title = _("Critical if older than"))
                               ]
                     ),
            ),
            ("unspec",
                Tuple(
                    title = _("Specify time since last successful unspecific backup"),
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

