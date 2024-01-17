
import random
from turtle import Screen, Turtle


#funcion para dibujar un cuadrado usando el objeto creado my_turtile
def square(my_turtle):
    
    #importamosla funcion que creamos para cambiar el color aleatoriamente
    change_color(my_turtle)
    
    for i in range(4):
        # Girar la tortuga a la izquierda
        my_turtle.right(90)
        
        #moviendo hacia el frente
        my_turtle.forward(100)
        
              

# Esta función cambia el color de una tortuga de forma aleatoria
def change_color(my_turtle):
    
    # Genera un número aleatorio entre 0 y 1 para la componente roja del color
    R=random.random()   
    
    # Genera un número aleatorio entre 0 y 1 para la componente azul del color
    B=random.random()
    
    # Genera un número aleatorio entre 0 y 1 para la componente verde del color
    G=random.random()
    
    # Asigna el color generado a la tortuga usando el método color
    my_turtle.color(R,G,B)

 
#funcion para dibujar triangulo            
def triangle(my_turtle):
    
    #importamosla funcion que creamos para cambiar el color aleatoriamente
    change_color(my_turtle)
    
    #hacemos un ciclo for, para repetir nuestro codigo 3 veces
    for i in range(3):
        
        #movemos la orientacion de la tortuga 120 grados con respecto al eje 'x'
        my_turtle.right(120)
    
        #mviendo hacia el frente 10 piezas 
        my_turtle.forward(100)
    
    
# Esta función dibuja un pentágono con una tortuga de un color aleatorio
def pentagon(my_turtle):
    
    # Llama a la función change_color para cambiar el color de la tortuga
    change_color(my_turtle)
    
    # Repite cinco veces el siguiente bloque de código
    for i in range(5):
        # Gira la tortuga 72 grados a la derecha
        my_turtle.right(72)
        # Avanza la tortuga 100 unidades
        my_turtle.forward(100)

  
 # Esta función dibuja un hexagon con una tortuga de un color aleatorio
def hexagon(my_turtle):
    
    # Llama a la función change_color para cambiar el color de la tortuga
    change_color(my_turtle)
    
    # Repite seis  veces el siguiente bloque de código
    for i in range(6):
        # Gira la tortuga 60 grados a la derecha
        my_turtle.right(60)
        
        # Avanza la tortuga 100 unidades
        my_turtle.forward(100)
 

 # Esta función dibuja un heptagono con una tortuga de un color aleatorio
def heptagon(my_turtle):
    
    # Llama a la función change_color para cambiar el color de la tortuga
    change_color(my_turtle)
    
    # Repite siete  veces el siguiente bloque de código
    for i in range(7):
        # Gira la tortuga 51,42.... grados a la derecha
        my_turtle.right(360/7)
        
        # Avanza la tortuga 100 unidades
        my_turtle.forward(100)
    
        
# Esta función dibuja un heptagono con una tortuga de un color aleatorio
def octagon(my_turtle):
    
    # Llama a la función change_color para cambiar el color de la tortuga
    change_color(my_turtle)
    
    # Repite ocho  veces el siguiente bloque de código
    for i in range(8):
        # Gira la tortuga .... grados a la derecha
        my_turtle.right(360/8)
        
        # Avanza la tortuga 100 unidades
        my_turtle.forward(100)        
        
        
# Esta función dibuja un nonagono con una tortuga de un color aleatorio
def nonagon(my_turtle):
    
    # Llama a la función change_color para cambiar el color de la tortuga
    change_color(my_turtle)
    
    # Repite nueve veces el siguiente bloque de código
    for i in range(9):
        
        # Gira la tortuga .... grados a la derecha
        my_turtle.right(360/9)
        
        # Avanza la tortuga 100 unidades
        my_turtle.forward(100)          
   
# Esta función dibuja un nonagono con una tortuga de un color aleatorio
def decagono(my_turtle):
    
    # Llama a la función change_color para cambiar el color de la tortuga
    change_color(my_turtle)
    
    # Repite diez veces el siguiente bloque de código
    for i in range(10):
        
        # Gira la tortuga .... grados a la derecha
        my_turtle.right(360/10)
        
        # Avanza la tortuga 100 unidades
        my_turtle.forward(100)          
           
        
def geometric_figures(my_turtle):
    
    triangle(my_turtle)
    
    square(my_turtle)
    
    pentagon(my_turtle)  
            
    hexagon(my_turtle)
    
    heptagon(my_turtle)
    
    octagon(my_turtle)
    
    nonagon(my_turtle)
    
    decagono(my_turtle)
                
#creamos un objeto de la clase turtle
my_turtle = Turtle()

#cambiamos la firgura de nuestro objetoa tortuga
my_turtle.shape("turtle")

geometric_figures(my_turtle)







#permite que el programa continue corriendo hasta que hagamos click en la pantalla , debemos crear un objeto de la clase Screen() para usar el metodo exitonclick()
#debe ir al final de nuestro codigo
my_screen =Screen()
my_screen.exitonclick()