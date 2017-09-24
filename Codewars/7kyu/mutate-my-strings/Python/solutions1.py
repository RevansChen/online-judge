# Python - 3.4.3

def mutate_my_strings(s1, s2):
    results = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            results.append(s2[:i] + s1[i:])
    if len(results):
        if results[-1] != s2:
            results.append(s2)
    else:
        results.append(s2)
    return '\n'.join(results) + '\n'