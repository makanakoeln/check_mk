#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import config
import views, time, dashboard
import pagetypes, table
import sites

import livestatus
import notifications
from valuespec import *
from lib import *
import cmk.paths
import cmk.store as store

def get_user_overview_data(extra_filter_headers):

    host_comment_query     = "GET comments\n" \
                             "Stats: author = %s\n" \
                             "Stats: host_acknowledged > 0\n" \
                             "StatsAnd: 2\n" % (config.user.id)

    svc_comment_query      = "GET comments\n" \
                             "Stats: author = %s\n" \
                             "Stats: service_acknowledged > 0\n" \
                             "StatsAnd: 2\n" % (config.user.id)

    # nagios core has noch column "downtime_reccuring" so we have to 
    # take different lql for different cores

    if cmk.paths._get_core_name() == "cmc":
        down_host_query    = "GET downtimes\n" \
                             "Stats: host_scheduled_downtime_depth > 0\n" \
                             "Stats: downtime_recurring = 0\n" \
                             "Stats: service_scheduled_downtime_depth = 0\n" \
                             "StatsAnd: 3\n"

        down_service_query = "GET downtimes\n" \
                             "Stats: service_scheduled_downtime_depth > 0\n" \
                             "Stats: downtime_recurring = 0\n" \
                             "Stats: host_scheduled_downtime_depth = 0\n" \
                             "StatsAnd: 3\n"

    else:
        down_host_query    = "GET downtimes\n" \
                             "Stats: host_scheduled_downtime_depth > 0\n" \
                             "Stats: service_scheduled_downtime_depth = 0\n" \
                             "StatsAnd: 2\n"

        down_service_query = "GET downtimes\n" \
                             "Stats: service_scheduled_downtime_depth > 0\n" \
                             "Stats: host_scheduled_downtime_depth = 0\n" \
                             "StatsAnd: 2\n"

    try:
        host_commentdata = sites.live().query_summed_stats(host_comment_query)
        svc_commentdata = sites.live().query_summed_stats(svc_comment_query)
        down_host = sites.live().query_summed_stats(down_host_query)
        down_service = sites.live().query_summed_stats(down_service_query)

    except livestatus.MKLivestatusNotFoundError:
        return None, None, None, None
    else:
        return host_commentdata, svc_commentdata, down_host, down_service

def render_user_overview(extra_filter_headers="", extra_url_variables=None):
    #####################################
    # define what username to show 	#
    # Options: 				#
    # None == ID			#
    # "ALIAS" == alias			#
    # "NAME" == firstname surname	#
    #####################################
    show_user = "ALIAS"

    if show_user:
        if show_user == "NAME":
            if len(config.user.alias.split(",")) > 1:
                lastname, surname = config.user.alias.split(",")
                title_ack = "Acknowledged by %s. %s:" % ( surname[1], lastname )
            else:
                title_ack = "Acknowledged by %s:" % config.user.alias
        elif show_user == "ALIAS":
            title_ack = "Acknowledged by %s:" % config.user.alias
    else:
        title_ack = "Acknowledged by %s:" % config.user.id

    if extra_url_variables is None:
        extra_url_variables = []

    host_commentdata, svc_commentdata, down_host, down_service = get_user_overview_data(extra_filter_headers)
    

    if host_commentdata is None or svc_commentdata is None or down_host is None or down_service is None:
        html.center(_("No data from any site"))
        return

    td_class = 'col3'

    rows = [
        {
            "title" : _("Host problems"),
            "data"  : host_commentdata,
            "views" : {
                "all"       : [
                    ("view_name", "hostproblems_ack_by_author"),
                    ("search", "Search"),
                    ("filled_in", "filter"),
                    ("comment_author", config.user.id),
                ],
            },
        },
        {
            "title" : _("Service problems"),
            "data"  : svc_commentdata,
            "views" : {
                "all"       : [
                    ("view_name", "svcproblems_ack_by_author"),
                    ("search", "Search"),
                    ("filled_in", "filter"),
                    ("comment_author", config.user.id),
                ],
            },
        },
        {
            "title" : _("Current downtimes"),
            "data"  : svc_commentdata,
        },
        {
            "title" : _("Host downtimes"),
            "data"  : down_host,
            "views" : {
                "all"       : [
                    ("view_name", "hostdowntimes_by_author"),
                ],
            },
        },
        {
            "title" : _("Service downtimes"),
            "data"  : down_service,
            "views" : {
                "all"       : [
                    ("view_name", "svcdowntimes_by_author"),
                ],
            },
        },
    ]

    html.open_table(class_=["content_left", "user_overview"], cellspacing=3, cellpadding=0, border=0)
    html.open_tr()
    html.th(title_ack, style="color: #ffffff; text-align: left")
    html.close_tr()
    html.open_tr()
    html.close_tr()

    for row in rows:
        if row["title"] == "Current downtimes":
            html.open_tr()
            html.close_tr()
            html.open_tr()
            html.th(row["title"], style="color: #ffffff; text-align: left")
            html.close_tr()
            html.open_tr()
            html.close_tr()
        else:
            url = html.makeuri_contextless(row["views"]["all"] + extra_url_variables,filename="view.py")
            amount = row["data"]

            html.open_tr()
            html.th(row["title"])
            for value in amount:
                html.open_td(class_=[td_class, "states prob" if value != 0 else None])
                link(str(value), url)
            html.close_td()
            html.close_td()
            html.close_tr()

    html.close_table()


snapin_user_overview_styles = """
table.user_overview {
   border-collapse: separate;
   width: %dpx;
   margin-top: -7px;
}
table.user_overview th {
    font-size: 9pt;
    line-height: 7pt;
    text-align: left;
    color: #123a4a;
    font-weight: normal;
    padding: 0;
    padding-top: 2px;
    vertical-align: bottom;
}
table.user_overview td {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    font-family: arial, helvetica, sans-serif;
    width: 33.3%%;
    color: #ffffff;
    text-align: center;
    /* border: 1px solid #123a4a; */
    background-color: #6da1b8;
    padding: 0px;
    height: 14px;
    /* box-shadow: 1px 0px 1px #386068; */
}
table.user_overview td.prob {
    box-shadow: 0px 0px 4px #ffd000;
}
table.user_overview a { display: block; margin-right: 2px; }
""" % snapin_width


sidebar_snapins["user_overview"] = {
    "title" : _("User Overview"),
    "description" : _("Total number of acknowledged problems of current user and downtimes systemwide."),
    "refresh" : True,
    "render" : render_user_overview,
    "allowed" : [ "user", "admin", "guest" ],
    "styles" : snapin_user_overview_styles,
}

