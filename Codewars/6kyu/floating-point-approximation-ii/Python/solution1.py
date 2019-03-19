# Python - 3.6.0

interp = lambda f, l, u, n: [__import__('math').floor(f(l + (u - l) / n * i) * 100) / 100 for i in range(n)]
