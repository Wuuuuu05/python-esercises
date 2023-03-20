def f(*arg):
  result = 0
  for num in arg:
    result += num
  return result

print(f(1, 2, 3))
print(f(1, 2, 3, 4, 5)) 
