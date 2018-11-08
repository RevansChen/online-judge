# Python3

import re

class Node:
    def __init__(self):
        self.name = ''
        self.attrs = []
        self.elements = []

def formatNode(node, step = 0):
    results = [f'{"--" * step}{node.name}({", ".join(sorted(node.attrs))})']
    for e in node.elements:
        results.extend(formatNode(e, step + 1))
    return results

def xmlTags(xml):
    rootNode = None
    stack = []
    for start, name, attrStr, end in re.findall(r'<(\/?)(\w+)(.*?)(\/?)>', xml):
        if start == '/':
            stack.pop()
            continue

        attrs = re.findall(r'(\w*?)=', attrStr)

        if stack:
            currNode = stack[-1]

            nextNode = None
            for e in currNode.elements:
                if e.name == name:
                    nextNode = e
                    break

            if nextNode == None:
                nextNode = Node()
                nextNode.name = name
                currNode.elements.append(nextNode)

            for attr in attrs:
                if not attr in nextNode.attrs:
                    nextNode.attrs.append(attr)

            if end != '/':
                stack.append(nextNode)

        else:
            rootNode = Node()
            rootNode.name = name
            rootNode.attrs = attrs
            stack.append(rootNode)

    return formatNode(rootNode)
