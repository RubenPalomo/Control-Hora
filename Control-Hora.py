import time

def main():
    tiempo_segundos = time.time()
    tiempo_cadena = time.ctime(tiempo_segundos)
    tiempo_cadena = tiempo_cadena.split(" ")
    hora = tiempo_cadena[3]
    hora_pelada = hora.split(":")
    print(controlHora(int(hora_pelada[0])))
    

def controlHora(hora):
    if (hora >= 19):
        return "Hora de ir a casa."
    else:
        return f'Quedan {19 - hora} horas para ir a casa.'

if (__name__ == "__main__"):
    main()
