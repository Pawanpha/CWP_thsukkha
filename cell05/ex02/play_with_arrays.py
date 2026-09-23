#!/usr/bin/env python3

origin_arr = [2, 8, 9, 48, 8, 22, -12, 2]
print(origin_arr)
new_arr = [x + 2 for x in origin_arr if x > 5]
print(new_arr)