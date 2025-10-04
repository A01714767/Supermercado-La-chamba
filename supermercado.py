# Lista de productos y precios
precios = {
    "pan": 1.00,
    "leche": 1.50,
    "arroz": 2.00,
    "huevos": 2.50,
    "manzana": 0.75
}

total = 0
productos_comprados = []

print("Bienvenido al autocobro del supermercado.")
print("Productos disponibles y sus precios:")
for producto, precio in precios.items():
    print(f"- {producto.capitalize()}: ${precio:.2f}")
print("Escribe los productos que tienes uno por uno.")
print("Escribe 'fin' cuando termines.\n")

while True:
    producto = input("Producto: ").lower()
    if producto == "fin":
        break
    if producto in precios:
        total += precios[producto]
        productos_comprados.append(producto)
        print(f"{producto} agregado. Precio: ${precios[producto]:.2f}")
    else:
        print("Producto no reconocido. Intenta nuevamente.")

respuesta = input("¿Es usted persona de la tercera edad? (si/no): ").lower()
if respuesta == "si": 
    descuento = total * 0.10   
    total -= descuento
    print(f"Se aplicó un descuento de ${descuento:.2f}")

def mostrar_ticket(productos_comprados, total):
    print("--- Ticket de compra ---")
    for producto in productos_comprados:
        print(f"{producto.capitalize()} - ${precios[producto]:.2f}")
    print(f"Total a pagar: ${total:.2f}")
    print("------------------------")

mostrar_ticket(productos_comprados, total)


