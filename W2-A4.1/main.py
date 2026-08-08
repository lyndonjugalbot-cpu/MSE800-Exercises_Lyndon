# Assigning a list to a slice replaces exactly that slice with the new list's
#2 elements (5, 7) are replaced by 4 elements (-3, -9, -11, -13)
my_list = [1, 3, 5, 7, 9, 11]
my_list[2:4] = [-3, -9, -11, -13]
print(my_list)
#Result: [1, 3, -3, -9, -11, -13, 9, 11
#now contains 8 elements (indices 0-7), so index 4 is the middle.
my_list[4:4] = [100, 102, 104, 106, 108, 110]
print(my_list)
# Result: [1, 3, -3, -9, 100, 102, 104, 106, 108, 110, -11, -13, 9, 11]
