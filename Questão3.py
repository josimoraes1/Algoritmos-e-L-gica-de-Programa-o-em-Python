espacoInt=str(input()).upper()
portMalas=str(input()).upper()
valor=float(input())
motor=float(input())
cambio=str(input()).upper()

if espacoInt == "A" and portMalas == "G":

    if valor <= 100000 and motor >= 1.5 and cambio == "A":
      print("Pode comprar!")
    elif (valor <= 100000 and motor >= 1.5) or (valor <= 100000 and cambio == "A") or (cambio == "A" and motor >= 1.5):
      print("Boa compra.")
    elif (valor <= 100000 and motor < 1.5 and cambio != "A") or (valor > 100000 and motor >= 1.5 and cambio != "A") or (valor > 100000 and motor < 1.5 and cambio == "A"):
      print("Pode ser uma opção.")
    else:
        print("Recomendo pensar melhor...")
else:
    print("Não compre!")
