from random import choice

def sacarNumero():
  n = str(choice(range(1,13)))

  if n == '1':
    n = 'As'
  if n == '10':
    n = 'Sota'
  if n == '11':
    n = 'Caballo'
  if n == '12':
    n = 'Rey'

  return n

def sacarPalo():
  p = choice(range(1,5))

  if p == 1:
    p = " de Oros"
  if p == 2:
    p = " de Copas"
  if p == 3:
    p = " de Espadas"
  if p == 4:
    p = " de Bastos"

  return p

def sacarCarta():
  print(sacarNumero()+sacarPalo())

while True:
  print("¿Robar carta? <s/n>")
  a = input()

  if a == 's' or a == 'S':
    sacarCarta()
    print("")
  elif a == 'n' or a == 'N':
    break;
  else:
    print("Por favor introduce un parámetro válido <s/n>\n")