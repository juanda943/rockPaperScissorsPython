victoriasHumano =0
victoriasMaquina =0

print("_______________Piedra, Papel o Tijera__________________")
print("Bienvenidx")
print("iniciando el juego...")
seguirJugando = True
while seguirJugando:
    import random

    seleccionMaquina = random.choice(['Piedra', 'Papel', 'Tijera'])
    print("Mechas elijió "+ seleccionMaquina)
    seleccionHumano= random.choice(['Piedra', 'Papel', 'Tijera'])
    print("Nico elijió "+ seleccionHumano)

    if ((seleccionHumano=="Papel" and seleccionMaquina=="Piedra") or (seleccionHumano=="Tijera" and seleccionMaquina=="Papel") or (seleccionHumano=="Piedra" and seleccionMaquina=="Tijera")):
        victoriasHumano+=1
        print("Gano Nico")
    elif(seleccionMaquina==seleccionHumano):
        print("Empate")
    else:
        victoriasMaquina+=1
        print("Gano mechas")
    print("\n ¿Desean seguir jugando?")
    respuesta = input()
    if respuesta == "no":
        seguirJugando= False
        print("\n Gracias por jugar UwU")
        print("Puntaje de Nico ---> "+ str(victoriasHumano))
        print("Puntaje Mechas ----> "+ str(victoriasMaquina))
    
