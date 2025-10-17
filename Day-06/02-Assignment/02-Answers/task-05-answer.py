my_list = [1, 2, 3, 4, 5]

# Identity operators
a = my_list
b = [1, 2, 3, 4, 5]

is_same_object = a is my_list
is_not_same_object = b is not my_list

# Membership operators
element_in_list = 3 in my_list
element_not_in_list = 6 not in my_list

print("a is my_list:", is_same_object)
print("b is not my_list:", is_not_same_object)
print("3 in my_list:", element_in_list)
print("6 not in my_list:", element_not_in_list)
-------

my_list = ["sam", "mahe", "sid", "lachi", "mustafa"]

my_copy = my_list
global_list = []

is_same_object = my_copy is my_list
is_not_same_object = global_list is my_list

element_in_list = "sam" in my_list
element_not_in_list = "navya" in my_list

print("list is my_list:", is_same_object)
print("global_list is my_list:", is_not_same_object)
print("sam in my_list:", element_in_list)
print("navya in my_list:", element_not_in_list)
------
output:

list is my_list: True
global_list is my_list: False
sam in my_list: True
navya in my_list: False
