# Python - 3.6.0

def Xbonacci(signature, n):
    l = len(signature)
    i = 0
    while n > len(signature):
        signature.append(sum(signature[i:i + l]))
        i += 1
    return signature[0:n]
