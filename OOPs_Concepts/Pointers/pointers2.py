dict1 ={
    'val1':10
}

dict2 = dict1

print("Before dict2 value is updated : ")
print(f"dict1 = {dict1}, dict2 = {dict2}")

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2['val1'] = 20

print("\nAfter dict2 value is updated : ")
print(f"dict1 = {dict1}, dict2 = {dict2}")

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))