# Python - 2.7.6

Test.assert_equals(eval_object({'a': 1, 'b': 1, 'operation': '+'}), 2, 'Return the evaluated string as a number!')
Test.assert_equals(eval_object({'a': 1, 'b': 1, 'operation': '-'}), 0, 'Return the evaluated string as a number!')
Test.assert_equals(eval_object({'a': 1, 'b': 1, 'operation': '/'}), 1, 'Return the evaluated string as a number!')
Test.assert_equals(eval_object({'a': 1, 'b': 1, 'operation': '*'}), 1, 'Return the evaluated string as a number!')
Test.assert_equals(eval_object({'a': 1, 'b': 1, 'operation': '%'}), 0, 'Return the evaluated string as a number!')
Test.assert_equals(eval_object({'a': 1, 'b': 1, 'operation': '**'}), 1, 'Return the evaluated string as a number!')
