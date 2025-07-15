import random  

# ---------------------------
# Funcion principal - Solicitud de Datos
# ---------------------------

def ingresar_datos_iniciales():
    MAX_BUSES = 80
    MAX_LINEAS = 40
    buses = int(input("Ingrese la cantidad de buses (máx 80): "))
    while buses < 1 or buses > MAX_BUSES:
        buses = int(input("Cantidad inválida. Ingrese nuevamente: "))

    lineas = int(input("Ingrese la cantidad de líneas (máx 40): "))
    while lineas < 1 or lineas > MAX_LINEAS:
        lineas = int(input("Cantidad inválida. Ingrese nuevamente: "))

    matriz = generar_recaudacion(buses, lineas)
    return buses, lineas, matriz

# ---------------------------
# Funcion generativa de recaudaciones    
# ---------------------------


def generar_recaudacion(buses, lineas):
    matriz = []
    for i in range(buses):
        fila = []
        for j in range(lineas):
            fila.append(random.randint(5000, 12000)) 
        matriz.append(fila)     
    return matriz    



# ---------------------------
# Funcion para Menú de la empresa
# ---------------------------
def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Ver recaudaciones")
    print("2. Bus(es) con mayor recaudación total")
    print("3. Bus(es) con mayor recaudación por línea")
    print("4. Línea con menor recaudación por bus")
    print("5. Ordenar buses por recaudación total")
    print("6. Buscar recaudación de un bus en una línea")
    print("7. Intercambiar recaudación entre 2 buses")
    print("8. Verificador de buses rentables")
    print("9. Salir")


# ---------------------------
# Funcion Menú 01 - Para ver recaudaciones
# ---------------------------

def ver_recaudaciones(matriz):
    for i in range(len(matriz)):
        print("Bus", i + 1, ":", matriz[i])

# ---------------------------
# Funcion Menú 02 -Para ver quien tiene mayor dinero en total
# ---------------------------
def bus_mayor_recaudacion_total(matriz):  
    totales = []  
    for i in range(len(matriz)):  
        total = 0 
        for j in range(len(matriz[i])): 
            total += matriz[i][j]  
        totales.append([i, total])  

    mayor = totales[0][1]  
    for k in range(len(totales)): 
        if totales[k][1] > mayor:  
            mayor = totales[k][1]  

    print("Bus(es) con mayor recaudación total:")  
    for k in range(len(totales)):  
        if totales[k][1] == mayor:  
            print("Bus", totales[k][0] + 1, "con recaudación de", mayor, "soles")  

        
# ---------------------------
# Funcion Menú 03 - Para ver quien tiene mayor por linea      
# ---------------------------

def bus_mayor_por_linea(matriz):
    lineas = len(matriz[0])
    buses = len(matriz)
    for j in range(lineas):
        mayor = matriz[0][j]
        for i in range(buses):
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
        print("\nLínea", j + 1, ":")
        for i in range(buses):
            if matriz[i][j] == mayor:
                print("  Bus", i + 1, "con", mayor, "soles")


# ---------------------------
# Funcion Menú 04 - Para ver quien tiene menor dinero    
# ---------------------------


def linea_menor_por_bus(matriz):
    for i in range(len(matriz)):
        menor = matriz[i][0]
        for j in range(len(matriz[i])):
            if matriz[i][j] < menor:
                menor = matriz[i][j]
        print("\nBus", i + 1, ":")
        for j in range(len(matriz[i])):
            if matriz[i][j] == menor:
                print("  Línea", j + 1, "con", menor, "soles")


# ---------------------------
# Funcion Menú 05 - Ordenamiento por el total de mayor a menor - con aplicacion burbuja
# ---------------------------

def ordenar_buses_por_total(matriz):
    totales = []
    for i in range(len(matriz)):
        total = 0
        for j in range(len(matriz[i])):
            total += matriz[i][j]
        totales.append([i, total])

    for i in range(len(totales) - 1):
        for j in range(i + 1, len(totales)):
            if totales[i][1] < totales[j][1]:
                totales[i], totales[j] = totales[j], totales[i]

    print("\nBuses ordenados por recaudación total:")
    for k in range(len(totales)):
        print("Bus", totales[k][0] + 1, ":", totales[k][1], "soles")



# ---------------------------
# Funcion Menú 06 - Aqui es para crear como un tipo buscador de recaudaciones
# ---------------------------

def buscar_recaudacion(matriz, buses, lineas):
    bus = int(input(f"Ingrese número de bus (1 a {buses}): ")) - 1
    linea = int(input(f"Ingrese número de línea (1 a {lineas}): ")) - 1
    if 0 <= bus < buses and 0 <= linea < lineas:
        print(f"Recaudación: {matriz[bus][linea]} soles")
    else:
        print("Datos fuera de rango.")


# ---------------------------
# Funcion Menú 07 - Para hacer el intercambio de recaudaciones entre buses
# ---------------------------



def intercambiar_recaudacion(matriz, buses, lineas):
    bus1 = int(input(f"Bus 1 (1 a {buses}): ")) - 1
    bus2 = int(input(f"Bus 2 (1 a {buses}): ")) - 1
    linea = int(input(f"Línea (1 a {lineas}): ")) - 1

    if 0 <= bus1 < buses and 0 <= bus2 < buses and 0 <= linea < lineas:
        matriz[bus1][linea], matriz[bus2][linea] = matriz[bus2][linea], matriz[bus1][linea]
        print("Intercambio realizado correctamente.")
    else:
        print("Datos fuera de rango.")


# ---------------------------
#  Funcion Menú 08 - Funcion recursiva - Verificar dependiendo la cantidad propuesta la rentabilidad
# ---------------------------

def contador_rentabilidad(matriz, buses, lineas):
    minimo = int(input("Ingrese el monto mínimo esperado por bus: "))
    cantidad = contar_recursiva(matriz, 0, minimo, buses, lineas)
    print(f"Hay {cantidad} bus(es) que superan los {minimo} soles de recaudación total.")


def contar_recursiva(matriz, i, minimo, buses, lineas):
    if i == buses:
        return 0 

    total = 0
    for j in range(lineas):  
        total += matriz[i][j]
    if total >= minimo:
        return 1 + contar_recursiva(matriz, i + 1, minimo, buses, lineas)
    else:
        return contar_recursiva(matriz, i + 1, minimo, buses, lineas)


# ---------------------------
# Funcion Menú 09 y Principal - Demostracion de los datos y despedidad del programa.
# ---------------------------

buses, lineas, matriz = ingresar_datos_iniciales()

opcion = 0
while opcion != 9:
    mostrar_menu()
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        ver_recaudaciones(matriz)
    elif opcion == 2:
        bus_mayor_recaudacion_total(matriz)
    elif opcion == 3:
        bus_mayor_por_linea(matriz)
    elif opcion == 4:
        linea_menor_por_bus(matriz)
    elif opcion == 5:
        ordenar_buses_por_total(matriz)
    elif opcion == 6:
        buscar_recaudacion(matriz, buses, lineas)
    elif opcion == 7:
        intercambiar_recaudacion(matriz, buses, lineas)
    elif opcion == 8:
        contador_rentabilidad(matriz, buses, lineas)
    elif opcion == 9:
        print("Gracias por usar el sistema.")
    else:
        print("Opción inválida. Intente de nuevo.")
