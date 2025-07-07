import random

def obtener_palabra_secreta():
    palabras = ['python','javascript','java','angular','tensorflow','react','typescript','git','flask']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta,letras_adivinadas):
    adivinado = ''
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado
    
    
    
def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False
    
    print("Bienvenido al juego delahorcado")
    print(f"tenes {intentos} intentos para adivinar la palabra secreta.")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas), "la cantida de letras de la palabra es:", len(palabra_secreta))
    
    
    while not juego_terminado and intentos > 0:
        letra = input("introduce una letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor introduzca una letra valida (solo escribir una letra)")
            
        elif letra in letras_adivinadas:
            print("ya has utilizado esa letra, prueba con otra")
            
        else:
            letras_adivinadas.append(letra)
            
            if letra in palabra_secreta:
                print(f"Muy bien has acertado, la letra '{letra}' esta en la palabra.")
            else:
                intentos -=1
                print(f"lo siento, la letra '{letra}' no esta en la palabra.")
                print(f"te quedan {intentos} intentos.")
        
        progreso_actual = mostrar_progreso(palabra_secreta,letras_adivinadas)
        print(progreso_actual)
        
        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_secreta.capitalize()
            print(f"Felicitaciones has ganado!, la palabra completa es: '{palabra_secreta}'.")
    if intentos == 0:
        print(f"lo siento se te han acabado los intentos, la palabra secreta era: '{palabra_secreta}'.")

juego_ahorcado()        
    
