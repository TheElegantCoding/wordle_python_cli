from style.color import color

def print_title():
  print("Bienvenido a " + color.BOLD_GREEN + "WORDLE!" + color.RESET)

def print_instruction():
  print("")
  print("Instrucciones:")
  print("")
  print("1.- Introduce una palabra de cuatro letras en el teclado")
  print("2.- Después de cada intento las letras de la palabra introducida se colocaran de esta manera:")
  print(color.BOLD_GREEN + "    - Verde:" + color.RESET + " La letra está en la posición correcta")
  print(color.BOLD_YELLOW + "    - Amarillo:" + color.RESET + " La letra pertenece a la palabra pero esta en la posición incorrecta")
  print(color.BOLD_GRAY + "    - Gris: " + color.RESET + "La letra no esta en la palabra")
  print("3.- Solo tienes 3 vidas     para adivinar la palabra")
  print("")
  input("EMPEZAR A JUGAR YA! (Presiona enter para continuar...) ")