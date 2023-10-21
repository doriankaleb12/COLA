MaxTamC = 10
A = [0] * MaxTamC
frente = 0
final = 0
contador = 0

# Inicializar la cola
frente = 0
final = 0

respuesta = input("¿Desea agregar elementos a la cola? (s/n): ")

while (respuesta.lower() == 's' and contador < 10):
    if (final + 1) % MaxTamC == frente:
        print("\nDesbordamiento de la cola")
        break

    entrada = input("\nIngrese un elemento para la cola: ")
    try:
        elemento = int(entrada)
    except ValueError:
        print("Entrada no válida. Introduzca un número entero.")
        continue

    final = (final + 1) % MaxTamC
    A[final] = elemento

    contador += 1
    print("Elemento {} agregado a la cola: {}".format(contador, elemento))

    if contador < 10:
        respuesta = input("¿Desea agregar más elementos a la cola? (s/n): ")

# Validar si la cola está vacía
if frente == final:
    print("La cola está vacía.")
else:
    # Obtener el primer elemento de la cola
    primerElemento = A[(frente + 1) % MaxTamC]
    print("El primer elemento de la cola es:", primerElemento)

    # Eliminar un elemento de la cola (avanzar el frente)
    frente = (frente + 1) % MaxTamC

    # Imprimir elementos de la cola en el orden en que fueron ingresados
    print("Elementos de la cola en el orden de ingreso:")
    i = (frente + 1) % MaxTamC
    while i != (final + 1) % MaxTamC:
        print(A[i], end=" ")
        i = (i + 1) % MaxTamC
    print()

