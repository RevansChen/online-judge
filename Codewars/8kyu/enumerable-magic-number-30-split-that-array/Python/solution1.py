# Python - 3.6.0

partition = lambda list, classifier_method: ([*filter(classifier_method, list)], [*__import__('itertools').filterfalse(classifier_method, list)])

