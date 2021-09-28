x = ['', 4, True, 5, False, 'string2', True, 9.5, 'string3']

y = []


# segédlistával a példa alapján
def fuggveny1():
    for p in x:
        if type(p) is str:
            y.append('string')
        if type(p) is int:
            y.append('integer')
        if type(p) is bool:
            y.append('boolean')
        if type(p) is float:
            y.append('float')
    print(y)


# segédlista nélkül
# forrás: https://careerkarma.com/blog/python-replace-item-in-list/
def fuggveny2():
    for index, p in enumerate(x):
        if type(p) is str:
            x[index] = ('string')
        if type(p) is int:
            x[index] = ('integer')
        if type(p) is bool:
            x[index] = ('boolean')
        if type(p) is float:
            x[index] = ('float')
    print(x)


fuggveny1()
fuggveny2()