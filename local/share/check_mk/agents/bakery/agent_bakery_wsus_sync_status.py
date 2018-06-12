#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

group = "agents/" + _("Own Plugins")

register_rule(group,
    "agent_config:wsus_sync_status",
    CascadingDropdown(
        title = _("Deploy WSUS Sync Status plugin (Windows)"),
        help = _("This will deploy the agent plugin <tt>wsus_sync_status.ps1</tt> for monitoring "
                 "the status of WSUS sync."),
        style = "dropdown",
        choices = [
            ( "activate", _("Deploy WSUS sync plugin, expect WSUS on the following port:"),
                Integer(
                    default_value = 8530 ,
                    minvalue = 1,
                    maxvalue = 65535,
                    orientation = "horizontal",
            )),
            ( "disabled", _("Do not deploy WSUS sync plugin") ),
        ]
    ),
)
