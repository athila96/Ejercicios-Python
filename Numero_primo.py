""" 
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 """

# Indica si un numero es o no primo
def numero_primo(numero):
     if numero <= 1:
          return False

     divisores = [2,3,5,7,11,13]

     for primo in divisores:
          if primo >= numero:
               break
          if numero % primo == 0:
              return False
    
     return True
               
        
for numeros in range(1, 101):
     if numero_primo(numeros):
          print(numeros, end=",")
              
          
