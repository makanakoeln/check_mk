#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

group = "agents/" + _("Own Plugins")

register_rule(group,
    "agent_config:last_windows_updates",
    DropdownChoice(
        title = _("Last windows updates (Windows)"),
        help = _("This will deploy the agent plugin <tt>last_windows_updates.vbs</tt> for monitoring "
                 "the date of the last windows update."),
        choices = [
                    ( True,   _("Deploy last windows update plugin") ),
                    ( False, _("Do not deploy last windows update plugin") ),
        ]
    )
)
