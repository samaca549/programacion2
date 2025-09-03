
#hallar mcm 
numero1=int(input("digite un numero para el mcm"))
numero2=int(input("digite un numero para el mcm"))
lista=[]
lista2=[]

n=2
while numero1 > 1:
        if numero1 % n == 0:
            lista.append(n)
            numero1 = numero1 // n
        else:
            n += 1

i=2
while numero2 > 1:
        if numero2 % i == 0:
            lista2.append(i)
            numero2 = numero2 // i
        else:
            i += 1
 
        

print(lista)
print(lista2)

