tipoImovel=str(input()).upper()
qtdDias=int(input())
diasTV=int(input())
diasInternet=int(input())
valorTotal=0

if tipoImovel == "STANDARD":
    valorTotal = (150*qtdDias)+(10*diasTV)+(15*diasInternet)
    print("%.2f" %valorTotal)
else:
    valorTotal = (200 * qtdDias) + (10 * diasTV) + (15 * diasInternet)
    print("%.2f" % valorTotal)