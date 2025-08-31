# Lista de productos y precios
precios = {
    "pan": 1.00,
    "leche": 1.50,
    "arroz": 2.00,
    "huevos": 2.50,
    "manzana": 0.75
}

total = 0

print("Bienvenido al autocobro del supermercado.")
print("Escribe los productos que tienes uno por uno.")
print("Escribe 'fin' cuando termines.\n")

while True:
    producto = input("Producto: ").lower()
    if producto == "fin":
        break
    if producto in precios:
        total += precios[producto]
        print(f"{producto} agregado. Precio: ${precios[producto]:.2f}")
    else:
        print("Producto no reconocido. Intenta nuevamente.")

# Preguntar si es persona de la tercera edad
respuesta = input("\n¿Es usted persona de la tercera edad? (si/no): ").lower()

if respuesta == "si":
    descuento = total * 0.10   # 10% de descuento
    total -= descuento
    print(f"Se aplicó un descuento de ${descuento:.2f}")

print(f"\nTotal a pagar: ${total:.2f}")
print("Gracias por tu compra.")


