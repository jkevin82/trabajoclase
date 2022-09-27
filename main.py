"""Viaje
en bus
El
precio de un viaje en bus viene dado por la siguiente
función
𝑌=1.5𝑥+4
Donde
‘ representa el precio final y ‘ los kilómetros
recorridos, antes de pasar a la siguiente diapositiva
intenta por tu cuenta diseñar una función que tome
como parámetro ‘ y retorne el valor de ‘
def viaje(x):
  y=1.5*x+4
  return (y)
km=float(input("Digite los kilometros recorridos:  "))
precio=viaje(km)
print(f"el precio total es {precio}")

#################################################
Hacer un programa en PYTHON que permita al usuario elegir calcular: suma, resta, multiplicación y división entre dos números.


def menu():
  print("------------------------")
  print("Suma")
  print("Resta")
  print("Multiplicacion")
  print("Division")

def suma():
  num1=int(input("Digite un numero:  "))
  num2=int(input("Digite otro numero:  "))
  op=num1+num2
  return op
def resta():
  num1=int(input("Digite un numero:  "))
  num2=int(input("Digite otro numero:  "))
  op=num1-num2
  return op
def multiplicacion():
  num1=int(input("Digite un numero:  "))
  num2=int(input("Digite otro numero:  "))
  op=num1*num2
  return op
def division():
  num1=int(input("Digite un numero:  "))
  num2=int(input("Digite otro numero:  "))
  op=num1/num2
  return op
bandera=True
while bandera:
  menu()
  operacion=input("Que operacion desea realizar:").lower()
  if operacion=="suma":
    op=suma()
    print(op)
  elif operacion=="resta":
    op=resta()
    print(op)
  elif operacion=="multiplicacion":
    op=multiplicacion()
    print(op)
  elif operacion=="division":
    op=division()
    print(op)
#########################################
"""
def menu():
  print("------------------------")
  print("Que forma geometrica deseas")
  print("Circulo")
  print("Cuadrado")
  print("Triagulo")
  print("Rectangulo")
pi=3.1416
def circulo():
  r=int(input("Digite el radio:  ")) 
  r=round(r, 2)
  op= pi*r**2
  return op
def cuadrado():
  num1=int(input("Digite un lado:  "))
  num2=int(input("Digite el otro lado:  "))
  op=num1*num2
  return op
def triangulo():
  num1=int(input("Digite la base del triangulo:  "))
  num2=int(input("Digite la altura:  "))
  op=(num1*num2)/2
  return op
def rectangulo():
  num1=int(input("Digite la base del rectangulo:  "))
  num2=int(input("Digite la altura del rectangulo:  "))
  op=(num1*num2)
  return op
bandera=True
while bandera:
  menu()
  operacion=input("Que operacion desea realizar:").lower()
  if operacion=="circulo":
    op=circulo()
    print(op)
  elif operacion=="triangulo":
    op=triangulo()
    print(op)
  elif operacion=="rectangulo":
    op=rectangulo()
    print(op)
  elif operacion=="cuadrado":
    op=cuadrado()
    print(op)