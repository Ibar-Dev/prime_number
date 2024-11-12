"""Define una función llamada prime_numbers que tome un número entero positivo 
como parámetro y devuelva una lista con todos los números primos hasta ese número. 
Utiliza programación funcional y, en particular, la función filter para realizar la
verificación de primos."""


# def es_primo(numero):
#     if numero < 2:
#         return False

#     for n in range(2, int(numero** 0.5)+1 ):
        
#         if numero % n == 0:
#             return False
#     return True

# numero = int(input('Ingrese número: '))
# if es_primo(numero):
#     print(numero, "es un número primo")
# else:
#     print(numero, "no es un número primo")

def es_primo(numero):
    if numero < 2:
        return False

    for n in range(2, int(numero**0.5) + 1):
        if numero % n == 0:
            return False
    return True #Si llega aquí python entiende que se a ejecutado de manera correcta

def verificar_numeros():
    while True:
        numero = input('Ingrese número (o "salir" para terminar): ')
        
        if numero.lower() == 'salir':
            break
        
        try:
            numero = int(numero)
            if es_primo(numero): #Si es correcto y el programa se ejecura sin retornar False, 
                print(numero, "es un número primo")
            else:
                print(numero, "no es un número primo") #Si la funcion anterior se detiene en un "return False" entendera que no se ha finalizado la funcion anterior de manera completa
        except ValueError:
            print('Ingrese un número válido')

verificar_numeros()
