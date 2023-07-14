#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    Tuple,
    Integer,
    ListOfStrings,
    MonitoringState,
    TextAscii,
)

from cmk.gui.plugins.wato import (
    rulespec_registry,
    CheckParameterRulespecWithItem,
    RulespecGroupCheckParametersApplications,
)

def _item_spec_wsus_sync_status():
    return TextAscii(
        title = _("Service descriptions"),
        allow_empty = False,
    )

def _parameter_valuespec_wsus_sync_status():
    return Dictionary(
        elements = [
            ("wsus_sync", Tuple(
                    title = _("Specify time since last successful WSUS sync"),
                    elements = [
                        Age(title = _("Warning if older than")),
                        Age(title = _("Critical if older than"))
                    ]),
            ),
        ])

rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="wsus_sync_status",
        group=RulespecGroupCheckParametersApplications,
        item_spec=_item_spec_wsus_sync_status,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_wsus_sync_status,
        title=lambda: _("Time since last WSUS sync"),
    ))

