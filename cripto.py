word = str(input())
for letra in palavra:
  ords.append(ord(letra))

print("+ Encrypty message: ",*ords,sep=" ")
print("+ Original message: ",word)
