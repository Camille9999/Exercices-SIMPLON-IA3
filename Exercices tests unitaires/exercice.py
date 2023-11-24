def maxmin(string):
    list = string.split(' ')
    list_int = [int(nb) for nb in list]
    maximum = max(list_int)
    minimum = min(list_int)
    return f'{maximum} {minimum}'