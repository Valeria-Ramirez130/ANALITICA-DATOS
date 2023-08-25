print("Bienvenido AHORCADO.")

def ahorcado():
  cadena = str(input("Ahora Digite una palabra: "))
  cadenaMayuscula=cadena.upper()

  lista = list(cadenaMayuscula)

  return lista

palabra=ahorcado()

palabraOculta=[]

for i in range(0,len(palabra)):
  palabraOculta.append("_")

contador=0
vidas=5


x=1

while x!=0:
  print("Tienes ",vidas," vidas.")
  print(palabraOculta)
  letra=str(input("Digite una letra: "))[0]
  letraMayus=letra.upper()

  if letraMayus in palabra:
    print("La letra '",letraMayus,"' esta en la palabra.")

    for i in range(0,len(palabra)):
      if letraMayus == palabra[i]:
        palabraOculta[i]=palabra[i]
        contador+=1
        if contador==len(palabra):
          x=0
          print("Ganaste, lograste adivinar la palabra: ",palabra)

  else:
    vidas-=1
    print("La letra '",letraMayus,"' no esta en la palabra.")
    print("Te quedan ",vidas," vidas restantes.")
    if vidas==0:
      x=0
      print("Perdiste")

  print("\n")