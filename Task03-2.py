string = input("Input a website：")
new_string = string.split("//")[-1].split("/")[0]
print(new_string)
