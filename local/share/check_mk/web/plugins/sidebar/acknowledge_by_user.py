import views, time, defaults, dashboard
from lib import *


# Python 2.3 does not have 'set' in normal namespace.
# But it can be imported from 'sets'
try:
    set()
except NameError:
    from sets import Set as set

def render_acknowledgegroup_overview():
    # Livestatus abfragen
    # Gruppen des jeweiligen Users abfragen
    
    #get_group_query = "GET contactgroups\nFilter: members >= %s\nColumns: name\n" % (config.user_id)
    # Kommentare des Users zaehlen
    
    comment_query = "GET comments\nStats: author = %s\nStats: service_acknowledged > 0\nStatsAnd: 2\n" % (config.user_id)

    try:
        #contacts = html.live.query_column(get_group_query)
        commentdata = html.live.query_summed_stats(comment_query)
    except livestatus.MKLivestatusNotFoundError:
        html.write("<center>No Data from any Site</center>")
        return

    #user_contact_groups = '|'.join(set(contacts))
    #if not user_contact_groups:
    #    user_contact_groups = "0"
    #elif "all" in user_contact_groups:
    #    user_contact_groups = "all"

    #get_groups = ""
    #count = 0
    #for a in set(contacts):
    #for a in user_contact_groups:
    #    get_groups += "\nStats: service_contact_groups >= " + a
    #    count +=1
    #group = "%s\nOr: %s" % (get_groups, count)

    #get_ack_query = "GET comments%s\nStats: service_acknowledged > 0\nStatsAnd: 2\n" % (group)
    
    #try:
    #    group_ack = html.live.query_summed_stats(get_ack_query)
    #except livestatus.MKLivestatusNotFoundError:
    #    sum = 0
    #    html.write("<table class=\"content_center acknowledgegroupoverview\" cellspacing=2 cellpadding=0 border=0>\n")
    #    html.write("<tr><th><center>%s<center></th></tr>\n" % ("by you"))
    #    html.write("<tr>")
    #    html.write('<td class=total><center><a target="main" href="view.py?filled_in=filter&view_name=%s&comment_author=%s">%d</a><center></td>' % ("svcproblems_by_author", config.user_id, commentdata[0]))
    #    html.write("<tr><th><center>%s<center></th></tr>\n" % ("by your contact group"))
    #    html.write("<tr>")
    #    html.write('<td class=total><center><a target="main" href="view.py?filled_in=filter&search=Search&view_name=%s&c=%s">%d</a><center></td>' % ("svcproblems_by_contactgroup", user_contact_groups, sum))
    #    return

    #sum = 0
    #for b in group_ack:
    #    sum += b

    html.write("<table class=\"content_center acknowledgegroupoverview\" cellspacing=2 cellpadding=0 border=0>\n")


    for title, data  in [
            (_("by you"), commentdata),
    #        (_("by your contact groups"), sum),
            ]:
        html.write("<tr><th><center>%s<center></th></tr>\n" % (title))
        html.write("<tr>")
        html.write("<tr>")


        #if title == "by your contact groups":
            #if sum == "0":
                #html.write('<td class=total><center><a target="main" href="view.py?filled_in=filter&search=Search&view_name=%s&c=%s">%d</a><center></td>' % ("svcproblems_by_contactgroup", user_contact_groups, sum))
            #else:
                #html.write('<td class=states prob><center><a target="main" href="view.py?filled_in=filter&search=Search&view_name=%s&c=%s">%d</a><center></td>' % ("svcproblems_by_contactgroup", user_contact_groups, sum))
        if title == "by you":
            if commentdata[0] == 0:
                html.write('<td class=total><center><a target="main" href="view.py?search=Search&filled_in=filter&view_name=%s&comment_author=%s">%d</a><center></td>' % ("svcproblems_by_author_incl_down_host", config.user_id, data[0]))
            else:
                html.write('<td class=states prob><center><a target="main" href="view.py?search=Search&filled_in=filter&view_name=%s&comment_author=%s">%d</a><center></td>' % ("svcproblems_by_author_incl_down_host", config.user_id, data[0])) 


        html.write("</tr>\n")
    html.write("</table>\n")

sidebar_snapins["acknowledgegroup_overview"] = {
    "title" : _("Acknowledged Problems"),
    "description" : _("The total number of acknowledge problems of users contact group"),
    "refresh" : True,
    "render" : render_acknowledgegroup_overview,
    "allowed" : [ "user", "admin", "guest" ],
    "styles" : """
table.acknowledgegroupoverview {
   border-collapse: separate;
   width: %dpx;
   margin-top: -7px;
}
table.acknowledgegroupoverview th {
    font-size: 9pt;
    line-height: 7pt;
    text-align: left;
    color: #123a4a;
    font-weight: normal;
    padding: 0;
    padding-top: 2px;
    vertical-align: bottom;
}
table.acknowledgegroupoverview td {
    width: 33.3%%;
    text-align: right;
    /* border: 1px solid #123a4a; */
    background-color: #6da1b8;
    padding: 0px;
    height: 14px;
    /* box-shadow: 1px 0px 1px #386068; */
}
table.acknowledgegroupoverview td.prob {
    box-shadow: 0px 0px 4px #ffd000;
}
table.acknowledgegroupoverview a { display: block; margin-right: 2px; }
""" % snapin_width
}
