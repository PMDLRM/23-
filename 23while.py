import turtle

def cosa_bonita(opcion):
    
    t = turtle.Turtle()
    t.pensize(5)
    t.forward(50)
    t.right(180)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(70)
    t.left(180)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.left(180)
    t.forward(30)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(30)
    t.right(180)
    t.forward(30)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(90)
    t.left(70)
    t.forward(50)
    t.left(220)
    t.forward(50)
    t.left(180)
    t.forward(25)
    t.left(70)
    t.forward(18)
    t.left(74)
    t.forward(26)
    t.left(107)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(140)
    t.forward(25)
    t.left(95)
    t.forward(25)
    t.right(135)
    t.forward(50)
    t.left(90)
    t.forward(30)
    t.circle(25)
    t.goto(-120,-60)
    t.color("red")
    t.begin_fill()
    t.fillcolor("red")
    t.left(140)
    t.forward(180)
    t.circle(-90,200)
    t.setheading(60)
    t.circle(-90,200)
    t.forward(180)
    t.end_fill()



def main():
    print("ADVERTENCIA: FAVOR DE INGRESAR LA CONTESTACIÓN LA PRIMER LETRA EN MAYÚSCULA Y LO DEMÁS EN MINÚSCULA, PAOLA SIGUE APRENDIENDO")
    print("Computadora: Hola")
    print("Funado: ",end="")
    contestacion = input()
#     if(contestacion=="Hola" or contestacion=="hola" or contestacion=="HOLA"):
    while(contestacion != "Hola"):
        print("No seas grosero, di hola")
        print("Funado: ",end="")
        contestacion = input()
    print("Veo que eres muy guapo, ¿te llamas David García León?")
    print("Funado: ",end="")
    sino = input()
    if (sino=="Si"):
            print("Genial, Paola te manda esto. ¡Felices 23 meses! (Se abrirá una ventana nueva, cuidado)")
            cosa_bonita(sino)
    else:
        print("Ah, bueno, esto no es para ti pues. Adiós")
        
main()