""" 
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 """

def fibonacci():
    resultado = 0 # 13
    variacion = 1 # 21
    for i in range(1, 50):
       print(resultado, end=",")
       
       fibonacci = resultado + variacion # 21
       resultado = variacion
       variacion = fibonacci
       
       
        
        

fibonacci()


""" 
Corrida en frio

  resultado: 0,1,1,2,3,5,8,
"""