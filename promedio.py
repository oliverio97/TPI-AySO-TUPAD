lista_notas = []
promedio = 0
print(
    "Bienvenido al programa para calcular promedios. Ingresá 3 notas para calcular el promedio de las mismas"
)

while True:
    for i in range(3):
        try:
            nota = float(input(f"Ingresa la nota {i+1}: "))
            lista_notas.append(nota)
        except ValueError:
            print("No has ingresado una opcion valida. Ingresa solamente numeros. \n")
            lista_notas = []
            break
    if len(lista_notas) == 3:
        break


for i in lista_notas:
    promedio += i

promedio /= 3

print(f"El promedio entre las notas es: {promedio}")
