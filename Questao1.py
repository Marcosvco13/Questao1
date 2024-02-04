#Questão 1

def inverter_diagonais(matriz):
    tamanho = len(matriz)

    for i in range(tamanho // 2):
        matriz[i][i], matriz[tamanho - 1 - i][tamanho - 1 - i] = matriz[tamanho - 1 - i][tamanho - 1 - i], matriz[i][i]
        matriz[i][tamanho - 1 - i], matriz[tamanho - 1 - i][i] = matriz[tamanho - 1 - i][i], matriz[i][tamanho - 1 - i]

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
for linha in matriz:
    print(linha)

inverter_diagonais(matriz)

print("Matriz invertida:")
for linha in matriz:
    print(linha)