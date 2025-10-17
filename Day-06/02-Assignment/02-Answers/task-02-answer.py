a = 10
b = 5

less_than = a < b
greater_than = a > b
less_than_or_equal = a <= b
greater_than_or_equal = a >= b
equal = a == b
not_equal = a != b

print("a < b:", less_than)
print("a > b:", greater_than)
print("a <= b:", less_than_or_equal)
print("a >= b:", greater_than_or_equal)
print("a == b:", equal)
print("a != b:", not_equal)

---
a = 10
b = 20

greater = a>b
less = a<b
equal = a==b
lessEqual = a<=b
greaterEqual = a>=b
notEqual = a!=b

print(greater, less, equal, lessEqual, greaterEqual, notEqual)

if greater:
  print(a, b)
else:
  print("a is less than b")

---
output:
False True False True False True
a is less than b
