# Python - 3.4.3

def mutate_my_strings(s1, s2):
    results = []
    # 只替換同位置但字不同的部分, 0 ~ n-1
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            results.append(s2[:i] + s1[i:])
    # 最後一個字的處理
    if len(results):
        if results[-1] != s2:
            results.append(s2)
    else:
        results.append(s2)
        
    # 每一個結果結尾都用'\n'分隔
    return '\n'.join(results) + '\n'