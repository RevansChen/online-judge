# Python3

import re

def pageComplexity(document):
    levels = {}
    stack = []
    maxDepth = -1
    for start, name, attrs, end in re.findall(r'<(\/?)(\w+)(.*?)(\/?)>', document):
        if start == '/':
            while stack:
                if stack.pop() == name:
                    break
        elif end != '/':
            stack.append(name)
            continue

        lv = len(stack)
        if not lv in levels:
            levels[lv] = set()
        levels[lv].add(name)
        maxDepth = max(maxDepth, len(stack))

    return sorted(list(levels.get(maxDepth, {})))
