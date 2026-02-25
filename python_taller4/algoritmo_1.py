import time
# Algoritmo 1
def obtener_elemento(lista):
    return lista[0]

# Algoritmo 2
def algoritmo_2(n):
    for i in range(n):
        print(i) 

# Algoritmo 3
def algoritmo_3(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

# Tamaños de prueba
lista_tamanos = list(range(10, 101, 10))  # 10,20,30,...,100

for n in lista_tamanos:

    print(f"\nProbando con n = {n}")

    # Medición algoritmo 1
    inicio = time.time()
    obtener_elemento(list(range(n)))
    fin = time.time()
    print("Tiempo Algoritmo 1:", fin - inicio)

    # Medición algoritmo 2
    inicio = time.time()
    algoritmo_2(n)
    fin = time.time()
    print("Tiempo Algoritmo 2:", fin - inicio)

    # Medición algoritmo 3
    inicio = time.time()
    algoritmo_3(n)
    fin = time.time()
    print("Tiempo Algoritmo 3:", fin - inicio)




