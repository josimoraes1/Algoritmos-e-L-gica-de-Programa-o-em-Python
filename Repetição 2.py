maiorSoma=0
maior=0
soma=0

for i in range(1, 6):
    m=int(input())
    soma=0
    for j in range(1, m+1):
        if m % j == 0:
            soma+=j
    if soma > maiorSoma:
        maiorSoma=soma
        maior=m

print(maior)
