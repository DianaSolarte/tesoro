jugador = input ("Bienvenidos a la isla del tesoro tu mision sera encontrar el tesoro, ¿cúal es tu nombre? ")
opc1 = input("¿escoges el camino de la derecha  o izquierda? ") # primera opción
opc1 = opc1.lower()


if(opc1== "derecha"):
    print("caiste en un agujero game over ") # primera opción

elif(opc1== "izquierda"): # primera opción
    print("Siguiente nivel") # primera opción
    opc2 = input("¿escoges el camino nadar  o esperar? ") # 2da opción
    opc2 = opc2.lower()

    if( opc2 == "nadar"): # 2da opción
        print("caiste en un agujero game over")
    elif (opc2=="esperar"):  # 2da opción 
        print("Siguiente nivel") # 2da opción
        opc3 = input("¿Camino de arañas o de serpientes? ") # 3ra opción
        opc3 = opc3.lower()

        if ( opc3 == "serpientes"): # 3ra opción
            print("Una serpiente te enveneno GAME OVER") # 3ra opción
        elif( opc3 =="arañas"): # 3ra opción
            print("Siguiente nivel")# 3ra opción3ta opción
            opc4 = input("¿Acabas de ver osos cerca. ¿Prefieres correr o caminar? ") # 4ta opción
            opc4 = opc4.lower()
