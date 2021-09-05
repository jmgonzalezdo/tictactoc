# -*- coding: utf-8 -*-
"""
Creado el Sabado 4 de Septiembre de 2021, 15:34:24

@autor: JOSE MANUEL GONZALEZ DOMINGUEZ
@email: jmgonzalezdo@gmail.com
@Curso: Python Entry-Level
@Centro Educativo: Kaans IT | Computer Technology 
"""
## *************************************
## **     Inicia sección de modulos   **
## *************************************
import random

## *************************************
## **     Inicia sección de variables **
## *************************************

Ganador = None
Combinacion_Gane = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
tablero = ['-' for x in range(9)]
partida = False


## *************************************
## **     Inicia sección de funciones **
## *************************************

def menu_principal():
    while True:
        print("*******************  (MENU)  ***********************")
        print("*************** Juego del Gato *********************")
        print("*    (1) - Jugador A vs Jugador B                  *")
        print("*    (2) - Jugador A vs Computadora (Fácil)        *")
        print("*    (3) - Jugador A vs Computadora (Dificil)      *")
        print("*    (4) - Salir                                   *")
        print("****************************************************")
        a = input("Elige una opción: ")
        try:
            a = int(a)
            if a in range(1, 5): # Solo puedo elegir del 1 al 4
                return a
            else: # En caso de que no eligio un número del 1 al 4
                print("\nEsto no es una opción valida, intenta otra vez")
                continue
        except ValueError: # en caso de que no tecleo un numero
            print("\nEsto no es un numero, intenta otra vez")
            continue

def TableroZero(): # Reinicia el tablero para volver a jugar.
    tzero = ['-' for x in range(10)]
    return tzero

def imprime_tabla(): 
    print("\n")
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2] + "     1 | 2 | 3")
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5] + "     4 | 5 | 6")
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8] + "     7 | 8 | 9")
    print("\n")

def Escoge_numero():
    while True:
        while True:
            a = input()
            try:
                a  = int(a)
                a -= 1
                if a in range(0, 9):
                    return a
                else:
                    print("\nOpcion no valida, intenta otra vez")
                    continue
            except ValueError:
               print("\nNo es un número, Intenta otra vez")
               continue

def Jugador_X():
    n = Escoge_numero()
    if tablero[n] == "X" or tablero[n] == "O":
        print("\nCasilla ocupada, Intenta otra vez")
        Jugador_X()
    else:
        tablero[n] = "X"
           
def Jugador_O():
    n = Escoge_numero()
    if tablero[n] == "X" or tablero[n] == "O":
        print("\nCasilla ocupada, Intenta otra vez")
        Jugador_O()
    else:
        tablero[n] = "O"
        
def validar_tablero():
    count = 0
    for a in Combinacion_Gane:
        if tablero[a[0]] == tablero[a[1]] == tablero[a[2]] == "X":
            ganador="X"
            print("Gano el jugador de las ",ganador,"!\n")
            print("Excelente juego!\n")
            return True

        if tablero[a[0]] == tablero[a[1]] == tablero[a[2]] == "O":
            ganador="O"
            print("Gano el jugador de las ",ganador,"!\n")
            print("Excelente juego!\n")
            return True
    for a in range(9):
        if tablero[a] == "X" or tablero[a] == "O":
            count += 1
        if count == 9:
            ganador=None
            print("GAME OVER, Juego Empatado\n")
            return True
    return False
        
def J1_vs_J2(): # (1) - Jugador A vs Jugador B    
    partida=False
    while partida==False:
        imprime_tabla()
        if partida == False:
            print("Jugador 1, elige un numero de casilla")
            Jugador_X()
            print()
            imprime_tabla()
            partida = validar_tablero()
            if partida == True:
                break
            print("Jugador 2, elige un numero de casilla")
            Jugador_O()
            print()
            partida = validar_tablero()
            if partida == True:
                break

def Computadora_Facil(): # Algoritmo Sencillo de selección
    EspLib=list()  
    for a in range(len(tablero)-1):
        if (tablero[a]=="-"):
            EspLib.append(a)    
    OpcionCompu=random.sample(EspLib, 1)
    tablero[OpcionCompu[0]]="O"
    print("La Computadora eligió ", OpcionCompu[0]+1)
    
def J1_vs_CompFacil(): # Eligio la opcion: (2) - Jugador A vs Computadora (Fácil)
    partida=False
    while partida==False:
        imprime_tabla()
        if partida == False:
            print("Jugador 1, elige un numero de casilla")
            Jugador_X()
            print()
            imprime_tabla()
            partida = validar_tablero()
            if partida == True:
                break
            Computadora_Facil()
            print()
            partida = validar_tablero()
            if partida == True:
                break
    
    
## *************************************
## ** I   inicia programa principal   **
## *************************************

opcion=None
while (opcion != 4): # Cuando el usuario elija 4, termina el programa
    opcion=menu_principal()
    if (opcion == 1): # Eligio la opcion  (1) - Jugador A vs Jugador B  
        tablero=TableroZero()
        J1_vs_J2()
        ## invocar funcion PLAYERVSPLAYER
        while True:       
            revancha=input("Deseas jugar otra vez (S/N)")
            try:
                revancha = str(revancha.upper())
                if (revancha == "S"):                
                    tablero=TableroZero()
                    J1_vs_J2()
                    ## invocar funcion PLAYER VS PLAYER
                elif (revancha == "N"):
                    break
                else:
                    print("Opcion no valida, intenta otra vez")
                    continue
            except ValueError:
                print("elige S para SI, y N para NO, intenta otra vez")
                continue
    elif (opcion == 2): #Eligio la opción: (2) - Jugador A vs Computadora (Fácil)
        tablero=TableroZero()
        J1_vs_CompFacil()
        ## invocar funcion PLAYERVSCOMPUTER EASY
        while True:       
            revancha=input("Deseas jugar otra vez (S/N)")
            try:
                revancha = str(revancha.upper())
                if (revancha == "S"):                
                    tablero=TableroZero()
                    J1_vs_CompFacil()
                    ## invocar funcion PLAYER VS COMPUTER EASY
                elif (revancha == "N"):
                    break
                else:
                    print("Opcion no valida, intenta otra vez")
                    continue
            except ValueError:
                print("elige S para SI, y N para NO, intenta otra vez")
                continue
    elif (opcion == 3): # Eligio la opcion: (3) - Jugador A vs Computadora (Dificil) 
        imprime_tabla()
        ## invocar funcion PLAYERVSCOMPUTER EASY
        while True:       
            revancha=input("Deseas jugar otra vez (S/N)")
            try:
                revancha = str(revancha.upper())
                if (revancha == "S"):                
                    imprime_tabla()
                    ## invocar funcion PLAYER VS COMPUTER EASY
                elif (revancha == "N"):
                    break
                else:
                    print("Opcion no valida, intenta otra vez")
                    continue
            except ValueError:
                print("elige S para SI, y N para NO, intenta otra vez")
                continue    
print("Hasta la vista baby")# Eligo la opcion: (4) - Salir 