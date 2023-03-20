def freq(text):
  freq = {}
  for char in text:
    if char not in freq:
      freq[char] = 1
    else:
      freq[char] += 1
  return freq

x = input("輸入一串文字：")
frenquency = freq(x)
print(frenquency)
