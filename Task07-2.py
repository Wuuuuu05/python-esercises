L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L1 = []
L2 = []

for x in L :
  if x % 2 == 0 :
    L1.append(x)
  else :
    L2.append(x)

L3 = L2 + L1
print(L3)
