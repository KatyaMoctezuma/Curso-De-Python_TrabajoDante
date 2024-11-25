numero_usuario = int(input("Por favor alumno, ingresa un número: "))

if numero_usuario == 0:
    print("El número ingresado es cero, no es ni par ni impar.")
elif numero_usuario % 2 == 0:
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar.")
