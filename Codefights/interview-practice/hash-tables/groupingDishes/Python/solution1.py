# Python3

def groupingDishes(dishes):
    ingredients = {}
    for name, *dish in dishes:
        for i in dish:
            if not i in ingredients:
                ingredients[i] = set()
            ingredients[i].add(name)

    ingredients = { k: v for k, v in ingredients.items() if len(v) > 1 }
    return [ [i] + sorted(list(ingredients[i])) for i in sorted([*ingredients.keys()]) ]
