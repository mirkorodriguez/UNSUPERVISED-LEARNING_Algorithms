import math

pesos = [[0.2, 0.6, 0.5, 0.9], [0.8, 0.4, 0.7, 0.3]]
dataset = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]]

print("pesos:",pesos)
print("dataset:",dataset)

lr = 0.6
epocas=100

for x in range(1, epocas+1):
    print('\n\n=================')
    print('Epoca: ', x,'/',epocas)
    print('=================')
    print('Learning Rate: ', lr)

    for i in range(0,4):
        d1 = math.sqrt(
        (pesos[0][0] - dataset[i][0])**2 +
        (pesos[0][1] - dataset[i][1])**2 +
        (pesos[0][2] - dataset[i][2])**2 +
        (pesos[0][3] - dataset[i][3])**2
        )

        d2 = math.sqrt(
        (pesos[1][0] - dataset[i][0])**2 +
        (pesos[1][1] - dataset[i][1])**2 +
        (pesos[1][2] - dataset[i][2])**2 +
        (pesos[1][3] - dataset[i][3])**2
        )

        print("\nDataset: ", dataset[i])
        print("Nodos: ", pesos)
        print("Distancia N1: ",d1,"\nDistancia N2: ", d2)

        for j in range(0,4):
            if d1 < d2:
                pesos[0][j] = pesos[0][j] + lr * (dataset[i][j] - pesos[0][j])
            else:
                pesos[1][j] = pesos[1][j] + lr * (dataset[i][j] - pesos[1][j])

        print("Pesos actualizados: ",pesos[0])
        print("Pesos actualizados: ",pesos[1])

    #Actualizamos el lr por cada epoca
    lr = 0.5*lr

print('\n==============')
print('Pesos finales:')
print('==============')
print([ round(elem, 1) for elem in pesos[0] ])
print([ round(elem, 1) for elem in pesos[1] ])

print('\n===========')
print('Agrupacion:')
print('===========')

for i in range(0,4):
    d1 = math.sqrt(
    (pesos[0][0] - dataset[i][0])**2 +
    (pesos[0][1] - dataset[i][1])**2 +
    (pesos[0][2] - dataset[i][2])**2 +
    (pesos[0][3] - dataset[i][3])**2
    )

    d2 = math.sqrt(
    (pesos[1][0] - dataset[i][0])**2 +
    (pesos[1][1] - dataset[i][1])**2 +
    (pesos[1][2] - dataset[i][2])**2 +
    (pesos[1][3] - dataset[i][3])**2
    )

    print("Data["+str(i)+"]:", dataset[i], end =" pertence al ")

    if d1 < d2:
        print("Grupo #1")
    else:
        print("Grupo #2")
