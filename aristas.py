import turtle
t=turtle.Pen()


    
n=int(input("ingrese un numero de lados "))


for x in range(n):
#va a delante hasta cuantas veces debe girar a la derecha
    t.forward(108)
    t.left((n-2)*180/n)
    t.left((n-2)*180/n)



   
turtle.getscreen()._root.mainloop()


#365 divido para el numero de lados
