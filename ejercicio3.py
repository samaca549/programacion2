def sumanumeros(x):
    x
    for i in range(1, 101):
        x=x+i
    print(x)

sumanumeros(1)

def sumanumeros2(x, y):
    y=int(input("digite  la cantidad de numeros que quiere sumar"))
    for i in range(1, y+1):
        x=x+i
    print(x)
    
sumanumeros2(1, 101)

def sumanumeros3(x, y):
    y=int(input("digite  la cantidad de numeros que quiere sumar"))
    for i in range(1, y+1):
        x=x+i
    print(x)
    return x
a=sumanumeros3(1, 101)
a=a+3
print(a)
moneda=float(input("digite la cantidad de euros que posee:"))
def eurosadolares(x):
    divisa=x*1.168
    print(f"la cantidad de dolares que usted tiene despues del cambio fueron {divisa} ")
eurosadolares(moneda)
base=float(input("digite el valor de la base:"))
altura=float(input("digite el valor de la altura:"))
def area(x, y):
    multiplicacion=x*y
    return multiplicacion
a=area(base, altura)
print(f"el resultado de la multiplicacion {a}")
a=a+1
print(a)

valor1=int(input("digite el valor 1:"))
valor2=int(input("digite el valor 2:"))
def mayor(x, y):
    if (x>y):
        print(f"el valor mayor es {x}")
    elif (y>x):
        print(f"el valor mayor es {y}")
    else:
        print(f"los valores son iguales")


mayor(valor1, valor2)

numeroimpar=int(input("digite el numero para hallar los numeros impares menores que el"))
y=[]
def impar(x):
    for i in range (x, 0, -1):
        if ((i%2)==1):
            y.append(i)

    print(y)
impar(numeroimpar)


