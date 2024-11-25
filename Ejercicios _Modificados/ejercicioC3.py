numero_ingresado = int(input("Por favor, ingresa un número: "))

if numero_ingresado > 20:
    print("El número ingresado es mayor que 20.")
elif numero_ingresado > 10:
    print("El número ingresado es mayor que 10 pero menor o igual a 20.")
elif numero_ingresado > 5:
    print("El número ingresado es mayor que 5 pero menor o igual a 10.")
else:
    print("El número ingresado es menor o igual a 5.")

