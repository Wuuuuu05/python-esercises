x = input("輸入一個數字：")

try:
  n = int(x)
except ValueError:
  print(f"{x} 是一個不合法的輸入，無法運算")
  exit()
  
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

result = factorial(n)
print(f"{n}! = {result}")
