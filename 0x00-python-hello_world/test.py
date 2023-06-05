#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
start_index = str.index('object')
lent = len('prigramming')
stop_index = str.index('programming') + len('programming')
substring = str[start_index:stop_index]
print(substring)


# min
py_indexx = str.index('with')
# ila
py_index = str.index('with') + len('with')
print(py_indexx)
print(py_index)
