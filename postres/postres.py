POSTRES = {}

def mostrar_ingredientes(nombre):
    if nombre in POSTRES:
        print(f"Ingredientes de {nombre}:")
        for ing in POSTRES[nombre]:
            print("-", ing)
    else:
        print("❌ El postre no existe")

def agregar_ingrediente(nombre, ingrediente):
    if nombre in POSTRES:
        if ingrediente not in POSTRES[nombre]:
            POSTRES[nombre].append(ingrediente)
            print("✅ Ingrediente agregado")
        else:
            print("⚠️ El ingrediente ya existe")
    else:
        print("❌ El postre no existe")

def eliminar_ingrediente(nombre, ingrediente):
    if nombre in POSTRES:
        if ingrediente in POSTRES[nombre]:
            POSTRES[nombre].remove(ingrediente)
            print("✅ Ingrediente eliminado")
        else:
            print("⚠️ El ingrediente no existe")
    else:
        print("❌ El postre no existe")

def agregar_postre(nombre, ingredientes):
    if nombre not in POSTRES:
        POSTRES[nombre] = ingredientes
        print("✅ Postre agregado")
    else:
        print("⚠️ El postre ya existe")

def eliminar_postre(nombre):
    if nombre in POSTRES:
        del POSTRES[nombre]
        print("✅ Postre eliminado")
    else:
        print("❌ El postre no existe")

def mostrar_todo():
    print("\n📌 Lista de POSTRES:")
    for postre, ingredientes in POSTRES.items():
        print(f"{postre}: {ingredientes}")

agregar_postre("Pastel", ["Harina", "Huevo", "Azúcar"])
agregar_postre("Gelatina", ["Agua", "Gelatina", "Azúcar"])

mostrar_todo()

mostrar_ingredientes("Pastel")

agregar_ingrediente("Pastel", "Leche")
eliminar_ingrediente("Pastel", "Huevo")

mostrar_ingredientes("Pastel")

eliminar_postre("Gelatina")

mostrar_todo()

def eliminar_repetidos():
    global POSTRES
    POSTRES = dict.fromkeys(POSTRES)
    print("✅ Repetidos eliminados")
    
