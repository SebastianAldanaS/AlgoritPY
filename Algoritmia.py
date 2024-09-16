import bisect

def encontrar_numeros(lista_base, consultas):
    resultados = []
    
    for consulta in consultas:
        pos_superior = bisect.bisect_right(lista_base, consulta)
        pos_inferior = bisect.bisect_left(lista_base, consulta) - 1
        
        # Determinar los valores correspondientes
        mayor_inferior = lista_base[pos_inferior] if pos_inferior >= 0 else 'X'
        menor_superior = lista_base[pos_superior] if pos_superior < len(lista_base) else 'X'
        
        resultados.append(f"{mayor_inferior} {menor_superior}")
    
    return resultados

# Entrada de datos
print("Ingrese un número entero con el tamaño de la lista de números a evaluar:")
tamaño_lista = int(input())  # Tamaño de la lista

print("Ingrese la lista de números separados por espacios:")
lista_base = list(map(int, input().split()))

# Validar que la cantidad de números en lista_base coincida con el tamaño proporcionado
if len(lista_base) != tamaño_lista:
    print("Error: El número de elementos en la lista no coincide con el tamaño ingresado.")
    exit()

print("Ingrese un número entero de consultas a evaluar:")
num_consultas = int(input())  # Número de consultas

print("Ingrese los números a evaluar en el algoritmo separados por espacios:")
consultas = list(map(int, input().split()))

# Validar que la cantidad de consultas coincida con el número proporcionado
if len(consultas) != num_consultas:
    print("Error: El número de consultas no coincide con el valor ingresado.")
    exit()

# Procesar las consultas y obtener los resultados
resultados = encontrar_numeros(lista_base, consultas)

# Imprimir resultados
for resultado in resultados:
    print(resultado)
