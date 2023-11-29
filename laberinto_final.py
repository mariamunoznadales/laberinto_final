def laberinto(dimension, muros):
   #La función ´laberinto´tiene dos argumentos: dimension (tamaño) y ´muros' (las coordenadas que representan las ubicaciones del los muros)

    # Lista vacía para añadir las filas del laberinto.
    laberinto = []
    # Bucle para recorrer las finales del laberinto
    # i toma valores de 0 a dimension-1 
    for i in range(dimension):
        # Lista para añadir las casillas de la fila.
        fila = []
        # Bucle para recorrer las columnas del laberinto.
        # j toma valores de 0 a dimension-1.
        for j in range(dimension):
            # Condicional para comprobar si la coordenada está en el la lista de muros.
            if tuple([i, j]) in muro:
                # Si la coordenada está en la lista de muros ponemos una X en la casilla.
                fila.append('X')
            else:
                # Si la coordenada no está en el muro ponemos un espacio en blanco en la casilla.
                fila.append(' ')
        laberinto.append(fila)
    return laberinto

# Conjunto de coordenadas de las celdas con muro 
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) 
juego = laberinto(5, muro) 

#Juntar todas las listas en una sola
for i in juego:
    print(''.join(i))

def mostrar_laberinto(juego):
    for fila in juego:
        print(' '.join(fila))
    print()

def mover_jugador(juego, direccion):
    jugador_posicion = encontrar_jugador(juego)
    x, y = jugador_posicion

    if direccion == 'arriba' and x > 0 and juego[x - 1][y] != 'X':
        juego[x][y] = ' '
        juego[x - 1][y] = 'P'
    elif direccion == 'abajo' and x < len(juego) - 1 and juego[x + 1][y] != 'X':
        juego[x][y] = ' '
        juego[x + 1][y] = 'P'
    elif direccion == 'izquierda' and y > 0 and juego[x][y - 1] != 'X':
        juego[x][y] = ' '
        juego[x][y - 1] = 'P'
    elif direccion == 'derecha' and y < len(juego[0]) - 1 and juego[x][y + 1] != 'X':
        juego[x][y] = ' '
        juego[x][y + 1] = 'P'

def encontrar_jugador(juego):
    for i in range(len(juego)):
        for j in range(len(juego[0])):
            if juego[i][j] == 'P':
                return i, j
             
# Conjunto de coordenadas de las celdas con muro 
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) 
juego = laberinto(5, muro)  

# Colocar al jugador en la posición inicial
juego[0][0] = 'P'
 

mostrar_laberinto(juego)

while True:
    direccion = input("Ingrese la dirección (arriba, abajo, izquierda, derecha): ")
    mover_jugador(juego, direccion)
    mostrar_laberinto(juego)

    # Verificar si el jugador ha llegado a la salida; Compara las coordenadas actuales del jugador con las coordenadas de la salida 
    # del laberinto. Si son iguales, significa que el jugador ha llegado a la salida del laberinto. 
    if encontrar_jugador(juego) == (len(juego) - 1, len(juego[0]) - 1):
        print("¡Felicidades! Has llegado a la salida.")
        break