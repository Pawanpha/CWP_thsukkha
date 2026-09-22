#!/usr/bin/env python3

original_arr = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array: " + str(original_arr))
new_arr = [x + 2 for x in original_arr]
print("New array: " + str(new_arr))