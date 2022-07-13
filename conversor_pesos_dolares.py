pesos_mexicanos = input("¿Cúantos pesos mexicanos tienes?: ")
pesos_mexicanos = float(pesos_mexicanos)
valor_dolar = 20.84
dolares = pesos_mexicanos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")