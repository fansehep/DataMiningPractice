#!/usr/bin/python3


import sys



print("--- Python import mode ---")
print("command args = ")
for i in sys.argv:
    print(i)
print("\n python path = ", sys.path)


a = 10
b = 1.23
c = a + b
print ("", c)
print (type(c))
