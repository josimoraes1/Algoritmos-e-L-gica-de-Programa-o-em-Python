mat=str(input())
cre=float(input())
menor = cre
soma=cre
matMenor=mat
cont=1

while True:
    mat = str(input())
    if mat == "999":
        break;
    else:
        cre=float(input())
        soma+=cre
        cont+=1
    if cre < menor:
        menor = cre
        matMenor = mat
print(matMenor)
print("%.2f" %(soma/cont))
