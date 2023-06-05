#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# min
strt = str.index('object')
# ila
endd = str.index('programming') + len('programming')
print(str[strt:endd])
