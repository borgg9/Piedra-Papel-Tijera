from tkinter import *
import random

raiz = Tk()
raiz.title('Piedra, papel o tijera...')

miFrame = Frame(raiz)

miFrame.pack()




# ------------------------MAQUINA----------------------------

# moviemineto de la maquina
def manoMaquina():
    
    global resultadoMaquina
    
    resultadoMaquina = ''
    elementos = [ 'Piedra', 'Papel', 'Tijera' ]
    
    
    resultadoMaquina = random.sample(elementos, 1)
    resultadoMaquina = resultadoMaquina[0]

    pantallaMaquina.set(resultadoMaquina)

# texto maquina
pantallaMaquina = StringVar() #imprimir en la pantalla

textoMaquina = Label(miFrame, text='Maquina:')
textoMaquina.grid(row=1, column=1)

maquina = Entry(miFrame, textvariable = pantallaMaquina)
maquina.grid(row=1, column=2, padx=10, pady=10, columnspan = 2)
maquina.config(background='black', fg='#03f943', justify='center')
                

                                  




                
    
    
# ------------------------JUGADOR----------------------------

# pulsar teclas
def manoJugador(num):
    
    global resultadoJugador
    global tirada
    
    pantallaJugador.set(num)  
    
    manoMaquina()  #cuando el jugador saca su mano, se simula la de la maquina
    
    resultadoJugador = ''
    resultadoJugador += num

    mostrarMarcador()     #cuando el jugador saca su mano, mostramos resultado

    numeroTirada()  #cuando el jugador saca su mano, se suma tirada           




    
# texto jugador
pantallaJugador = StringVar() #imprimir en la pantalla

textoJugador = Label(miFrame, text='Jugador:')
textoJugador.grid(row=4, column=1)

# pantalla
jugador = Entry(miFrame, textvariable = pantallaJugador)
jugador.grid(row=4, column=2, padx=10, pady=10, columnspan = 2)
jugador.config(background='black', fg='#03f943', justify='center') 

# botones
botonPiedra = Button(miFrame, text='Piedra', width = 6, padx=2, pady=2, command=lambda:manoJugador('Piedra'))
botonPiedra.grid(row=5, column=1)
botonPapel = Button(miFrame, text='Papel', width = 6, padx=2, pady=2, command=lambda:manoJugador('Papel'))
botonPapel.grid(row=5, column=2)
botonTijera = Button(miFrame, text='Tijera', width = 6, padx=2, pady=2, command=lambda:manoJugador('Tijera'))
botonTijera.grid(row=5, column=3)


                
                
# ------------------------MARCADOR 1 ----------------------------

marcador_maquina = 0
marcador_persona = 0
marcador_empate = 0

# calcular marcador
def mostrarMarcador():   
    mostrarResultados = ''
    
    global resultadoJugador
    global resultadoMaquina
    global marcador_maquina
    global marcador_persona
    global marcador_empate     
    
    # Empate
    if resultadoMaquina == resultadoJugador:
        marcador_empate += 1
        mostrarResultados = (str('Empate: ') + str(resultadoMaquina) + str(' Vs. ') + str(resultadoJugador))
    # Persona Piedra *
    elif resultadoMaquina == 'Papel' and resultadoJugador == 'Piedra':
        marcador_maquina += 1
        mostrarResultados = (str('Gana maquina: ') + str(resultadoMaquina) + str(' Vs. ') + str(resultadoJugador))

    elif resultadoMaquina == 'Tijera' and resultadoJugador == 'Piedra':
        marcador_persona += 1
        mostrarResultados = (str('Gana jugador: ') + str(resultadoMaquina) + str(' Vs. ') + str(resultadoJugador))

    # Persona Papel -
    elif resultadoMaquina == 'Piedra' and resultadoJugador == 'Papel':
        marcador_persona += 1
        mostrarResultados = (str('Gana jugador: ') + str(resultadoMaquina) + str(' Vs. ') + str(resultadoJugador))

    elif resultadoMaquina == 'Tijera' and resultadoJugador == 'Papel':
        marcador_maquina += 1
        mostrarResultados = (str('Gana maquina: ') + str(resultadoMaquina) + str(' Vs. ') + str(resultadoJugador))

    # Persona Tijera X
    elif resultadoMaquina == 'Papel' and resultadoJugador == 'Tijera':
        marcador_persona += 1
        mostrarResultados = (str('Gana jugador: ') + str(resultadoMaquina) + str(' Vs. ') + str(resultadoJugador))

    elif resultadoMaquina == 'Piedra' and resultadoJugador == 'Tijera':
        marcador_maquina += 1
        mostrarResultados = (str('Gana maquina: ') + str(resultadoMaquina) + str(' Vs. ') + str(resultadoJugador))

        
    pantallaMarcador.set(mostrarResultados) 
    
    
# texto maquina
pantallaMarcador = StringVar() #imprimir en la pantalla

# titulo marcador
#textoMarcador = Label(miFrame, text='Marcador:')
#textoMarcador.grid(row=2, column=1)

marcador = Entry(miFrame, width = 28,textvariable = pantallaMarcador)
marcador.grid(row=2, column=1, padx=10, pady=0, columnspan = 3)
marcador.config(background='black', fg='#03f943', justify='center')           



# ------------------------numero de tiradas + puntuacion  ----------------------------

tirada = 0

def numeroTirada():
    
    global tirada
    global marcador_maquina
    global marcador_persona
    global marcador_empate
   
    tirada += 1
    
    mostrarTiradas = (str(tirada) + ') Maquina: '+ str(marcador_maquina) + ' / ' + 'Jugador: ' + str(marcador_persona) + ' / Empate: ' + str(marcador_empate))
    pantallaTiradas.set(mostrarTiradas)
    
pantallaTiradas = StringVar() #imprimir en la pantalla
marcadorTiradas = Entry(miFrame, width = 28, textvariable = pantallaTiradas)
marcadorTiradas.grid(row=3, column=1, padx=10, pady=0, columnspan = 3)
marcadorTiradas.config(background='black', fg='#03f943', justify='center') 






           
raiz.mainloop()