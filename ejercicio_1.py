#Filtra los números que sean primos y cuadrados perfectos (como 4, 9, 16) de una lista de números
def es_primo(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

def es_cuadrado_perfecto(num):
    raiz = int(num ** 0.5)
    return raiz * raiz == num

numeros = list(range(1, 101))
primos_y_cuadrados = list(filter(lambda x: es_primo(x) and es_cuadrado_perfecto(x), numeros))
print(f"Números que son primos y cuadrados perfectos: {primos_y_cuadrados}")
