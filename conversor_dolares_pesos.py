dolares = input("¿Cúantos dólares tienes: ")
dolares = float(dolares)
valor_peso_mexicano = 0.048
pesos_mexicanos = dolares / valor_peso_mexicano
pesos_mexicanos = round(pesos_mexicanos, 2)
pesos_mexicanos = str(pesos_mexicanos)
print("Tienes $" + pesos_mexicanos + " pesos mexicanos")