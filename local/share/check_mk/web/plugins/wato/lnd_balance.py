#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

register_check_parameters(
    subgroup_applications,
    "lnd_balance",
    "Lightning Network Node - Balance",
    Dictionary(
        elements = [
            ( "balance_unit",
            DropdownChoice(
                title = "Show balance in satoshi or bitcoin",
                help = _("Helptext. "),
                choices = [
                    ( False,  _("satoshi") ),
                    ( True,  _("bitcoin") ),
                ])),
            ("levels_balance",
            Tuple(
                title = "Levels for total balance (sat)",
                help = _("Helptext. "),
                elements = [
                    Integer(title = "Warning below", default_value = 0, unit = _("satoshi")),
                    Integer(title = "Critical below", default_value = 0, unit = _("satoshi")),
                ])),
            ("levels_balance_confirmed",
            Tuple(
                title = "Levels for confirmed balance (sat)",
                help = _("Helptext. "),
                elements = [
                    Integer(title = "Warning below", default_value = 0, unit = _("satoshi")),
                    Integer(title = "Critical below", default_value = 0, unit = _("satoshi")),
                ])),
            ("levels_balance_unconfirmed",
            Tuple(
                title = "Levels for unconfirmed balance (sat)",
                help = _("Helptext. "),
                elements = [
                    Integer(title = "Warning above", default_value = 0, unit = _("satoshi")),
                    Integer(title = "Critical above", default_value = -1, unit = _("satoshi")),
                ])),
            ( "balance_diff",
            DropdownChoice(
                title = "Check for difference between total and confirmed balance",
                help = _("Helptext. "),
                choices = [
                    ( "1",  _("State: Warning") ),
                    ( "2",  _("State: Critical") ),
                ])),
        ]),
    None,
    "dict"
)

