import json

platos_por_defecto = [
    {"nombre": "Tortilla", "precio": 3.50, "categoria": "Tapas"},
    {"nombre": "Pizza", "precio": 10.50, "categoria": "Platos"},
    {"nombre": "Hamburguesa", "precio": 7.90, "categoria": "Platos"},
    {"nombre": "Agua", "precio": 1.50, "categoria": "Bebidas"},
]


def guardar_carta(carta):
    with open("carta.json", "w", encoding="utf-8") as f:
        json.dump(carta, f, ensure_ascii=False, indent=4)


def cargar_carta():
    try:
        with open("carta.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return list(platos_por_defecto)  # Devolver una copia de la lista por defecto


num = 0
carta = cargar_carta()

while num != 4:
    print("1. Ver carta \n2. Añadir plato \n3. Eliminar plato \n4. Salir")
    try:
        num = int(input("Elige una opción: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    if num == 1:
        if len(carta) == 0:
            print("La carta está vacía")
        else:
            for plato in carta:
                print(f"{plato['nombre']} - {plato['precio']:.2f}€ ({plato['categoria']})")

    elif num == 2:
        nombre = input("Introduce el plato que quieres añadir: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío")
            continue
        try:
            precio = float(input("Precio: "))
        except ValueError:
            print("El precio debe ser un número")
            continue
        if precio <= 0:
            print("El precio debe ser mayor que 0")
            continue
        categoria = input("Categoría: ").strip()
        nuevo_plato = {"nombre": nombre, "precio": precio, "categoria": categoria}
        carta.append(nuevo_plato)
        guardar_carta(carta)
        print("Plato añadido correctamente")

    elif num == 3:
        if len(carta) == 0:
            print("La carta está vacía")
            continue
        nombre = input("Nombre del plato a eliminar: ").strip()
        encontrado = False
        for plato in carta:
            if plato["nombre"].lower() == nombre.lower():
                carta.remove(plato)
                encontrado = True
                break
        if encontrado:
            guardar_carta(carta)
            print("Plato eliminado correctamente")
        else:
            print("No se ha encontrado ese plato")

    elif num == 4:
        print("Saliendo...")

    else:
        print("Opción no válida")