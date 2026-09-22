#!/usr/bin/env python3

number = float(input("Give me a number: "))

if number.is_integer():
    print(str(int(number)))
else:
    print(str(int(number) + 1))