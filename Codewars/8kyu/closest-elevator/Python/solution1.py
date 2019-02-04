# Python - 3.6.0

elevator = lambda left, right, call: 'right' if (abs(call - right) <= abs(call - left)) else 'left'
