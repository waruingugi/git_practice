# Custom map function

def custommap(func, iterable):
    new_list = []
    for i in iterable:
        new_list.append(func(i))

    return new_list

int_list = [6, 12, 18]
doubled = map(lambda input: input*2, int_list)
print(list(doubled))

custom_doubled = custommap(lambda input: input*2, int_list)
print(custom_doubled)
