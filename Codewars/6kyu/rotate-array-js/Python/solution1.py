# Python - 3.6.0

rotate = lambda arr, n: arr[-(n % len(arr)):] + arr[:-(n % len(arr))]
