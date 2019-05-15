# Python - 3.6.0

traffic_count = lambda array: [(f'{i + 4}:00pm', max(array[i * 6:(i + 1) * 6])) for i in range(4)]
