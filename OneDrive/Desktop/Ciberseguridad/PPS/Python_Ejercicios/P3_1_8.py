#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo
palabra = str(input("Introduce una palabra para ver si es un palindromo \n"))
if (palabra) == (palabra)[::-1]:
      print("Es Palindroma")
else:
      print("No es palindroma")

