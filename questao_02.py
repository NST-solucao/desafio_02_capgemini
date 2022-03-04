n = [1,5,3,4,2]
x = 2
iv = sorted(n, reverse=True)
t = len(n)
count = 0
for i in range(t):
    for element in iv:
        if iv[i] - element == x:
            # print(f'{iv[i]} - {element}') # Para testar retorno da subtração entre a lista[elementos]
            count+=1
print(count)
