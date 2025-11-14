import random
import time

vidas = 3

tiempo_limite = 30

frases = ['El sol brillaba fuerte mientras caminábamos por el parque.',
'Ayer cociné pasta con salsa roja y un poco de queso.',
'El perro corrió detrás de la pelota hasta cansarse completamente.',
'Me gusta escuchar música mientras dibujo o trabajo en casa.',
'Compramos pan, leche y frutas frescas en el supermercado cercano.',
'La lluvia caía suave sobre los árboles del jardín vacío.',
'Mañana iremos al cine a ver una película de acción.',
'El tren llegó tarde por culpa del mal tiempo en ruta.',
'Encendí la computadora y comencé a escribir sin parar un rato.',
'El gato dormía tranquilo sobre el sofá junto a la ventana.']

nombre = input("Ingrese nombre del jugador:")

print("==== Bienvenido", nombre, "al juego de Frases ====")
print("Tenes que escribir exactamente la frase que aparecerá debajo.")
print("Tenes 10 segundos para escribir cada frase.")

while vidas > 0:
    print("Te quedan", vidas, "vidas.")
    frase_juego = frases[random.randint(0,9)]
    print(frase_juego)
    inicio = time.time()
    frase_jugador = input("")
    fin = time.time()
    tiempo = fin - inicio
    if tiempo > tiempo_limite:
        print("Te quedaste sin tiempo")
    else:
        if frase_juego == frase_jugador:
            print("Felicitaciones!! Acertaste en tiempo y forma!!")
            break
        else:
            print("La frase no coincide.")
    vidas = vidas - 1

if vidas == 0:
    print("Lo lamento", nombre, "perdiste.")

with open('resultados.txt', 'a', encoding='UTF8') as f:
    if vidas > 0:
        if vidas == 1:
            linea = nombre + " ganó y le sobro " + str(vidas) + " vida.\n"
        else:
            linea = nombre + " ganó y le sobraron " + str(vidas) + " vidas.\n"
    else:
        linea = nombre + " se quedó sin vidas.\n"
    f.write(linea)