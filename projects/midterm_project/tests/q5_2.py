test = {   'name': 'q5_2',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> 'isWeekend' in covid_days.columns and 'dayOfWeek' in covid_days.columns\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> isinstance(covid_days.get('isWeekend').loc[0], np.bool_) or isinstance(covid_days.get('isWeekend').loc[0], bool) #the isWeekend column should "
                                               'contain True/False boolean values\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> list(covid_days.groupby('dayOfWeek').count().index)==['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday',\n"
                                               "...        'Wednesday'] #check spelling and capitalization\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
