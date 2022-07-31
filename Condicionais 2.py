salarioAtual=float(input())
percAum=0
valorAum=0
salFinal=0

if salarioAtual <= 280:

    percAum = 20
    valorAum = salarioAtual*0.2
    salFinal = salarioAtual + (salarioAtual*0.2)
    print("%.2f" %salarioAtual)
    print(percAum)
    print("%.2f" %valorAum)
    print("%.2f" % salFinal)

elif salarioAtual > 280 and salarioAtual <= 700:

    percAum = 15
    valorAum = salarioAtual * 0.15
    salFinal = salarioAtual + (salarioAtual * 0.15)
    print("%.2f" % salarioAtual)
    print(percAum)
    print("%.2f" % valorAum)
    print("%.2f" % salFinal)

elif salarioAtual > 700 and salarioAtual < 1500:

    percAum = 10
    valorAum = salarioAtual * 0.1
    salFinal = salarioAtual + (salarioAtual * 0.1)
    print("%.2f" % salarioAtual)
    print(percAum)
    print("%.2f" % valorAum)
    print("%.2f" % salFinal)

elif salarioAtual >= 1500:
    percAum = 5
    valorAum = salarioAtual * 0.05
    salFinal = salarioAtual + (salarioAtual * 0.05)
    print("%.2f" % salarioAtual)
    print(percAum)
    print("%.2f" % valorAum)
    print("%.2f" % salFinal)