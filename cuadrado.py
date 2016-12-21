import turtle
t=turtle.Pen()


    
n=int(input("ingrese un numero de lados "))
a=(365/n)


#delante
t.forward(50)
#izquierda
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
#gira  90 grados
t.left(90)
#y de ahi corre 50
t.forward(50)
t.reset()
for x in range(n):
#va a delante hasta cuantas veces debe girar a la derecha
    t.forward(100)
    t.left(a)
turtle.getscreen()._root.mainloop()


#365 divido para el numero de lados

