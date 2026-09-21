#!/usr/bin/env python3

age = int(input("Please tell me your age: "))

print("You are currently " + str(age) + " years old.")

for i in [10, 20, 30]:
    print("In " + str(i) + " years, you'll be " + str(age + i) + " years old.")