fat=0
corte=0
barba=0

while True:
    sexo=str(input()).lower()
    if sexo != "m" and sexo!= "f":
        break;
    else:
        serv=str(input()).lower()
    if sexo == "m":
        if serv == "corte":
            fat+= 25
            corte+=1
        elif serv == "barba":
            fat+= 15
            barba+=1

    elif sexo == "f":
        if serv == "corte":
            fat+= 40
        elif serv == "penteado":
            fat+= 50
        elif serv == "maquiagem":
            fat += 70
if corte>barba:
    print("CORTE")
elif corte == barba or (corte == 0 and barba == 0):
    print("AMBOS")
else:
    print("BARBA")
print("%.2f" %fat)
