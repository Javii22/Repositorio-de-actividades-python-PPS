# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio 
# de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	    0.85
# Naranja	0.70

precios: dict[str,float]={
    
    "Plátano":	1.35,
    "Manzana":	0.80,
    "Pera":	    0.85,
    "Naranja":	0.70                          
}

def precio_total(cantidad: float, fruta: str) -> float:
    return cantidad*precio_fruta(fruta)


def precio_fruta(fruta: str) -> float:
    #precios.get("fruta")
    return precios[fruta.lower().capitalize()]
    

if __name__ == "__main__":
    print("Fruteria Rafael\n")
    print("frutas del dia:")
    for frutas in precios.items():
        print(f"El kilo de {frutas[0]} cuesta {frutas[1]} €")

    while True:
        print("¿Que fruta quieres?: ")
        pedido: str=input().lower()
        if pedido == "morirme":
            break
        if pedido not in[key.lower() for key in precios.keys()]:
            print("No esta en la lista de frutas")
            continue
        print("¿cuantos Kilos?")
        flag: bool = True
        while flag:
            try:
                cantidad:float = float(input())
                flag = False
            except ValueError:
                print("Solo vale numeros")
        print(f"{cantidad} kgs de {pedido.capitalize} son {precio_total(cantidad,pedido)}")



        # Los test unitarios van unidos a los datos de prueba
        