#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    return (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])


tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
