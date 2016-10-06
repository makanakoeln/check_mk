#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# added option to also get check_mk agent data
# build within cmk 1.4.0i1

mk_jolokia_elements = [
   ( "agent",
                   DropdownChoice(
                       title = _("Type of query"),
                       choices = [
                           ( True,  _("Get also Check_MK Agent Data") ),
                           ( False, _("Only get jolokia output") ),
                       ],
                   )),
   ( "port",
     Integer(
         title = _("TCP port for connection"),
         default_value = 8080,
         minvalue = 1,
         maxvalue = 65535,
     )
   ),
   ( "login",
       Tuple(
           title = _("Optional login (if required)"),
           elements = [
             TextAscii(
                 title = _("User ID for web login (if login required)"),
                 default_value = "monitoring",
             ),
             Password(
                 title = _("Password for this user")
             ),
             DropdownChoice(
                 title = _("Login mode"),
                 choices = [
                    ( "basic",  _("HTTP Basic Authentication") ),
                    ( "digest", _("HTTP Digest") ),
                 ]
             )
           ]
       )
   ),
   ( "suburi",
     TextAscii(
         title = _("relative URI under which Jolokia is visible"),
         default_value = "jolokia",
         size = 30,
     )
   ),
   ( "instance",
     TextUnicode(
         title = _("Name of the instance in the monitoring"),
         help = _("If you do not specify a name here, then the TCP port number "
                  "will be used as an instance name.")
     ),
   ),
   ( "protocol",
     DropdownChoice(
         title = _("Protocol"),
         choices = [
             ( "http",  "HTTP" ),
             ( "https", "HTTPS" ),
         ]
     ),
   ),
]

group = 'datasource_programs'
register_rule(group,
    'special_agents:jolokia',
    Dictionary(
        elements = mk_jolokia_elements,
    ),
    title = _('Jolokia'),
    help = _('This rule allows querying the Jolokia web API.'),
    factory_default = FACTORY_DEFAULT_UNUSED, # No default, do not use setting if no rule matches
    match = 'first')
