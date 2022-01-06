#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from cmk.gui.i18n import _
from cmk.gui.plugins.wato import (
    HostRulespec,
    rulespec_registry,
)
from cmk.gui.cee.plugins.wato.agent_bakery.rulespecs.utils import RulespecGroupMonitoringAgentsAgentPlugins
from cmk.gui.valuespec import (
    Age,
    Alternative,
    Dictionary,
    FixedValue,
    ListOfStrings,
    TextAscii,
)

def _valuespec_agent_config_wsus_sync_status():
    return CascadingDropdown(
        title = _("Deploy WSUS Sync Status plugin (Windows)"),
        help = _("This will deploy the agent plugin <tt>wsus_sync_status.ps1</tt> for monitoring "
                 "the status of WSUS sync."),
        choices = [
            ( "activate", _("Deploy WSUS sync plugin, expect WSUS on the following port:"),
                Integer(
                    default_value = 8530 ,
                    minvalue = 1,
                    maxvalue = 65535,
            )),
            ( "disabled", _("Do not deploy WSUS sync plugin") ),
        ]
    )

rulespec_registry.register(
     HostRulespec(
         group=RulespecGroupMonitoringAgentsAgentPlugins,
         name="agent_config:wsus_sync_status",
         valuespec=_valuespec_agent_config_wsus_sync_status,
     ))
