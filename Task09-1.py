x = int(input("輸入一個正整數："))

def isPrime(n):
  if n > 1:
    for i in range(2,n):
      if n % i == 0:
        return False
        break
    else:
      return True
  else:
    return False

def primes(n):
  prime = []
  for i in range(2,n):
    if isPrime(i):
      prime.append(i)
  return prime

while isPrime(x) is True:
  print(f"{x} 是質數")
else:
  print(f"{x} 不是質數")
  
print(f"小於 {x} 的質數為 {primes(x)}")
  
