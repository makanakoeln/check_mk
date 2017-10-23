def paint_author_alias(userid):
    user_alias_query = "GET contacts\n" \
                       "Columns: alias\n" \
                       "Filter: name = %s\n" % userid
    user_alias = sites.live.query(user_alias_query)
    if user_alias:
        return user_alias[0][0]
    else:
        return userid

multisite_painters["comment_author_alias"] = {
        "title"   : _("Comment author alias"),
        "short"   : _("Author"),
        "columns" : ["comment_author"],
        "paint"   : lambda row: (None, paint_author_alias(row["comment_author"])),
}
