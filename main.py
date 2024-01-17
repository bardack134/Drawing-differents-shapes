
import random
from turtle import Screen, Turtle


                

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
  
           
        
def geometric_figures(my_turtle, grados):
    
       
    # Repite x veces el siguiente bloque de código, 'x' reporesenta el valor de grados en mi ciclo for 
    for i in range(grados):
        
        # Gira la tortuga .... grados a la derecha
        my_turtle.right(360/grados)
        
        # Avanza la tortuga 100 unidades
        my_turtle.forward(100) 
                
                
#creamos un objeto de la clase turtle
my_turtle = Turtle()

#cambiamos la firgura de nuestro objetoa tortuga
my_turtle.shape("turtle")

for grados  in range(3,11):
    
    # Llama a la función change_color para cambiar el color de la tortuga
    change_color(my_turtle)
    
    geometric_figures(my_turtle, grados)







#permite que el programa continue corriendo hasta que hagamos click en la pantalla , debemos crear un objeto de la clase Screen() para usar el metodo exitonclick()
#debe ir al final de nuestro codigo
my_screen =Screen()
my_screen.exitonclick()