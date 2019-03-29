# Python - 3.6.0

def warn_the_sheep(queue):
    wolf = len(queue) - queue.index('wolf') - 1
    return f'Oi! Sheep number {wolf}! You are about to be eaten by a wolf!' if wolf else 'Pls go away and stop eating my sheep'
