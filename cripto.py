palavra = str(input())
a=17
ords=[]
for letra in palavra:
    ords.append(ord(letra))

print("+ Mensagem c/ criptografia minima: ",*ords,sep=" ")
print("+ Mensagem original: ",palavra)