#!/usr/bin/env python3

origin_arr = [2, 8, 9, 48, 8, 22, -12, 2]
print(origin_arr)
new_arr = [y for x in origin_arr for y in [x + 2] if y > 5]
print(new_arr)