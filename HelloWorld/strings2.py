#                   1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6])  # Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14])
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # Bl
print(parrot[-14:-8])
print(parrot[-11:-9])
print(parrot[-14:-4])
print(parrot[-4:])
print(parrot[:-7])
print(parrot[-7:])


letters = "abcdefghijklmnopqrstuvwxyz"

print(letters[0])
print(letters[4])
print(letters[8])
print(letters[14])
print(letters[20])
print(letters[24])

print(parrot[0:6:2])    #Nre
print(parrot[0:6:3])    #Nw

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else "" for char in number).split()
print([int(val) for val in values])
