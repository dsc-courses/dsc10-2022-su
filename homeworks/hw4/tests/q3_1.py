test = {   'name': 'q3_1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> callable_test = callable(get_abbr) and callable(get_meaning)\n'
                                               ">>> dtype_test = (type(get_abbr('ROFL - Rolling on floor laughing')) == str) and (type(get_meaning('ROFL - Rolling on floor laughing')) == str)\n"
                                               '>>> callable_test and dtype_test\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> get_abbr("AFAIK - As far as I know") == "AFAIK" and get_meaning("AFAIK - As far as I know") == "As far as I know"\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
