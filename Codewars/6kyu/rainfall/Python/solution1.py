# Python - 3.6.0

def parse(strng):
    ds = {}
    citys = strng.split('\n')
    for city in citys:
        name, datas = city.split(':', 2)
        ds[name] = [float(data.split(' ')[1]) for data in datas.split(',')]
    return ds

def mean(town, strng):
    ds = parse(strng)
    if town in ds:
        return sum(ds[town]) / len(ds[town])
    return -1

def variance(town, strng):
    ds = parse(strng)
    if town in ds:
        m = sum(ds[town]) / len(ds[town])
        return sum([(d - m) ** 2 for d in ds[town]]) / len(ds[town])
    return -1
