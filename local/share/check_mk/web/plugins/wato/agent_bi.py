#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-


group = "datasource_programs"

register_rule(group,
    "special_agents:bi",
    Tuple(
        title = _("Check State of BI Aggregations"),
        help = _("Connect to the local or a remote monitoring host, which uses Check_MK BI to aggregate "
                 "several states to a single BI aggregation, which you want to show up as a single "
                 "service."),
        elements = [
            TextAscii(
                title = _("Base URL (OMD Site)"),
                help = _("The base URL to the monitoring instance. For example <tt>http://mycheckmk01/mysite</tt>. You can use "
                         "macros like <tt>$HOSTADDRESS$</tt> and <tt>$HOSTNAME$</tt> within this URL to make them be replaced by "
                         "the hosts values."),
                size = 60,
                allow_empty = False
            ),
            CascadingDropdown(
                          title = _("Type of query"),
                          help = _("Query all or a list of aggregations"),
                          choices = [
                              ( "all", _("Get all aggregations") ),
                              ( "list", _("Define aggregations to query"),
                                       ListOfStrings(orientation = "horizontal",allow_empty = False)),
                          ],
            ),
            TextAscii(
                title = _("Username"),
                help = _("The name of the user account to use for fetching the BI aggregation via HTTP. When "
                         "using the cookie based authentication mode (default), this must be a user where "
                         "authentication is set to \"Automation Secret\" based authentication."),
                allow_empty = False
            ),
            Password(
                title = _("Password / Secret"),
                help = _("Valid automation secret or password for the user, depending on the chosen "
                         "authentication mode."),
                allow_empty = False
            ),
            Dictionary(
                title = _("Optional parameters"),
                elements = [
                    ("prefix", CascadingDropdown(
                          title = _("Prefix"),
                          help = _("Set an optional prefix in front of the service description"),
                          choices = [
                              ( "none", _("No prefix - use only BI name as service description") ),
                              ( "old_local", _('Use old local script style "BI_Aggr_BI_NAME"')),
                              ( "old_check", _('Use old active check style "Aggr BI NAME"')),
                              ( "customer", _('Use aggregation group "Group: BI NAME"')),
                              ( "own", _('Define your own prefix "PREFIX BI NAME"'),
                                       TextAscii(orientation = "horizontal", allow_empty = False)),
                          ],
                    )),
                    ( "agent", DropdownChoice(
                           title = _("Type of query"),
                           help = _("Optional query of the check_mk agent data"),
                           choices = [
                               ( True,  _("Get also check_mk agent data") ),
                               ( False, _("Only get the list of bi aggregations") ),
                          ],
                    )),
                    ("auth_mode", DropdownChoice(
                        title = _('Authentication Mode'),
                        default_value = 'cookie',
                        choices = [
                            ('cookie', _('Form (Cookie) based')),
                            ('basic',  _('HTTP Basic')),
                            ('digest', _('HTTP Digest')),
                        ],
                    )),
                    ("timeout", Integer(
                        title = _("Seconds before connection times out"),
                        unit = _("sec"),
                        default_value = 60,
                                )),
                    ("in_downtime",
                      RadioChoice(
                          title = _("State, if BI aggregate is in scheduled downtime"),
                          orientation = "vertical",
                          choices = [
                            ( None, _("Use normal state, ignore downtime") ),
                            ( "ok", _("Force to be OK") ),
                            ( "warn", _("Force to be WARN, if aggregate is not OK") ),
                          ]
                    )),
                    ("acknowledged",
                      RadioChoice(
                          title = _("State, if BI aggregate is acknowledged"),
                          orientation = "vertical",
                          choices = [
                            ( None, _("Use normal state, ignore acknowledgement") ),
                            ( "ok", _("Force to be OK") ),
                            ( "warn", _("Force to be WARN, if aggregate is not OK") ),
                          ]
                    )),
                    ("track_downtimes",
                     Checkbox(
                        title = _("Track downtimes"),
                        label = _("Automatically track downtimes of aggregation"),
                        help = _("If this is active, the check will automatically go into downtime "
                                "whenever the aggregation does. This downtime is also cleaned up "
                                "automatically when the aggregation leaves downtime. "
                                "Downtimes you set manually for this check are unaffected."),
                    )),
                    ("track_ack",
                     Checkbox(
                        title = _("Track acknowledgements"),
                        label = _("Automatically track acknowledgement of aggregation"),
                        help = _("If this is active, the check will automatically be acknowledged "
                                "whenever the aggregation is in state acknowledged."),
                    )),
                ]
            ),
        ]
    ),
    match = 'all'
)
