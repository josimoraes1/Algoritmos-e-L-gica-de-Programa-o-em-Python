ensinoMedio=str(input()).upper()
enceja=str(input())
notaEnceja=int(input())
tipoEscola=str(input())
renda=float(input())

if ensinoMedio != "CLD" and ensinoMedio != "CVC" and ensinoMedio != "CSC" and ensinoMedio != "NCC":
    print("Informacao sobre ensino medio invalida")
    
elif ensinoMedio == "CLD":
    if enceja == "s":
        if notaEnceja >= 400:
            print("Voce terah direito a isencao")
        elif renda <= 1431 and tipoEscola == "PUB":
            print("Voce terah direito a isencao")
        else:
            print("Infelizmente voce nao tem direito a isencao")

    elif tipoEscola == "PUB" or tipoEscola == "PCB" or tipoEscola == "PPB":

        if renda <= 1431:
            print("Voce terah direito a isencao")
        else:
            print("Infelizmente voce nao tem direito a isencao")

    elif tipoEscola == "PSB" or tipoEscola == "PPS" or tipoEscola == "NFE":
            print("Infelizmente voce nao tem direito a isencao")

elif ensinoMedio == "CVC":
    if tipoEscola == "PUB":
        print("Voce terah direito a isencao")
    else:
        print("Infelizmente voce nao tem direito a isencao")

elif ensinoMedio == "NCC" or ensinoMedio == "CSC":
    print("Infelizmente voce nao tem direito a isencao")