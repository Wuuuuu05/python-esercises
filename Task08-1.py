x = int(input("輸入一個正整數："))
result = 0

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

for i in range(1,x+1):
  result += factorial(i)

print(f"1! + 2! + ⋯⋯ + {x}! = {result}")
