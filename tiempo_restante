import time 

Ahora = time.localtime()[3]
minutoAhora = time.localtime()[4]

hora = time.strptime("19:00"[:2],"%H")[3]
minuto = time.strptime("19:00"[:2],"%M")[3]

if Ahora > time.strptime("19:00"[:2],"%H")[3]  or Ahora < time.strptime("08:00"[:2],"%H")[3]:
    print("Es hora de ir a casa")
else:
    restante = time.strptime("19:00"[:2],"%H")[3] - Ahora
    print("El tiempo restante de trabajo es:",restante -1,"hora y",60 - minutoAhora, "minutos")
