# Python - 2.7.6

next_id = lambda arr: [i for i in range(max(arr) + 2) if i not in arr][0] if arr else 0
