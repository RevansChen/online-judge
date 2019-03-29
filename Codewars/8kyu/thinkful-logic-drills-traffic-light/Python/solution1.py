# Python - 3.6.0

lights = ['green', 'yellow', 'red']
update_light = lambda current: lights[(lights.index(current) + 1) % len(lights)]
