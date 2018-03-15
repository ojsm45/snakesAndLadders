import random

cantJug = 0

tablero =[[100,99,98,97,96,95,94,93,92,91],
          [81,82,83,84,85,86,87,88,89,90],
          [80,79,78,77,76,75,74,73,72,71],
          [61,62,63,64,65,66,67,68,69,70],
          [60,59,58,57,56,55,54,53,52,51],
          [41,42,43,44,45,46,47,48,49,50],
          [40,39,38,37,36,35,34,33,32,31],
          [21,22,23,24,25,26,27,28,29,30],
          [20,19,18,17,16,15,14,13,12,11],
          [1,2,3,4,5,6,7,8,9,10]
]

serpientes = {
	14:4,
	35:11,
	61:14,
	69:29,
	82:43,
	85:17,
	87:31,
	91:25,
	95:67,
	97:58
}

escaleras = {
	8:30,
	15:47,
	20:39,
	23:76,
	28:50,
	33:70,
	41:62,
	57:83,
	66:89,
	79:99
}

jugadores = [

]
	
posJugadores = {
	

}

def impTablero():
        global tablero,posJug
        for fila in tablero:
                #print("[ ")
                #print("\t",fila[0],"\t",fila[1],"\t",fila[2],"\t",fila[3],"\t",fila[4],"\t",fila[5],"\t",fila[6],"\t",fila[7],"\t",fila[8],"\t",fila[9])
                print(fila)
                #print(" ]")

def comprobarPos(pos):
        global escaleras, serpientes
        if pos >= 100:
                return 100
        if pos in escaleras:
                print("CAISTE EN UNA ESCALERA!")
                return escaleras.get(pos)
                
        if pos in serpientes:
                print("CAISTE EN UNA SERPIENTE!")
                return serpientes.get(pos)

        return pos

def juego():
        global jugadores,cantJug
        turno = 0
        while 1:
                print()
                print()
                print("============================================")
                print("Turno del jugador",jugadores[turno])

                #Quitar comentario para agregar pause al juego..!!!!
                #input("Presione enter para lanzar dado...")

                resDado = tirarDado()
                print("DADO: ",resDado)
                print("Posición antigua:",posJugadores[jugadores[turno]])
                posJugadores[jugadores[turno]] = comprobarPos(posJugadores[jugadores[turno]] + resDado)
                print("Nueva posición:",posJugadores[jugadores[turno]])

                if posJugadores[jugadores[turno]] == 100:
                        print("Jugador",jugadores[turno]," GANA!")
                        exit(1)
                
                if turno < cantJug:
                        turno += 1
                if turno == cantJug:
                        turno = 0
        

def iniciar():
        global jugadores,posJugadores,cantJug
        cantJug = int(input("Ingrese cantidad de jugadores:"))
        i=0
        turno = 0
        while i < cantJug:
                print("Ingrese nombre del jugador ",i+1,":")
                nombre = input()
                jugadores.append(nombre)
                posJugadores[nombre] = 0
                i+=1
        juego()
        

def tirarDado():
	return random.randint(1,6)

                
def run():
        print("ESCALERAS Y SERPIENTES")
        impTablero()


if __name__ == '__main__':
	run()
