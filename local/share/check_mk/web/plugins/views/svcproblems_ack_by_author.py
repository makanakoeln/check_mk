multisite_builtin_views.update({
    'svcproblems_ack_by_author': {'browser_reload': 30,
                                  'column_headers': 'pergroup',
                                  'context': {'comment': {'comment_author': ''},
                                              'in_downtime': {'is_in_downtime': '-1'},
                                              'service_acknowledged': {'is_service_acknowledged': '1'},
                                              'service_in_notification_period': {'is_service_in_notification_period': '-1'},
                                              'service_state_type': {'is_service_state_type': '-1'},
                                              'summary_host': {'is_summary_host': '0'},
                                              'svchardstate': {'hdst0': '',
                                                               'hdst1': 'on',
                                                               'hdst2': 'on',
                                                               'hdst3': '',
                                                               'hdstp': 'on'},
                                              'svcstate': {'st0': '',
                                                           'st1': 'on',
                                                           'st2': 'on',
                                                           'st3': '',
                                                           'stp': 'on'}},
                                  'datasource': 'comments',
                                  'description': u'',
                                  'force_checkboxes': False,
                                  'group_painters': [('comment_author_alias',
                                                      '',
                                                      'comment_author')],
                                  'hidden': True,
                                  'hidebutton': True,
                                  'icon': None,
                                  'layout': 'boxed',
                                  'linktitle': u'Service Problems by author',
                                  'mobile': False,
                                  'mustsearch': False,
                                  'name': 'svcproblems_ack_by_author',
                                  'num_columns': 1,
                                  'owner': '',
                                  'painters': [('service_state', None, None),
                                               ('host', 'hoststatus', None),
                                               ('service_description', 'service', None),
                                               ('svc_plugin_output', None, None),
                                               ('svc_comments', None, None),
                                               ('svc_state_age', None, None)],
                                  'play_sounds': False,
                                  'public': True,
                                  'single_infos': [],
                                  'sorters': [('comment_author',
                                               False),
                                              ('svcstate', True),
                                              ('stateage', True),
                                              ('site_host', False),
                                              ('svcdescr', False)],
                                  'title': u'Acknowledged Service Problems by author',
                                  'topic': u'Test',
                                  'user_sortable': True}})
