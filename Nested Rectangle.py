#import turtle library
import  turtle
#set background to black
turtle.bgcolor("black")
#set pencolor to orange
turtle.pencolor("yellow")
turtle.color("yellow","green")
#change pen shape
turtle.shape("turtle")
turtle.pensize(5)
#using loop
mycolor=["red","blue","yellow","green","orange"]
k=0
j=200
for i in range(0,17,1):
    turtle.pencolor(mycolor[k])
    k+=1
    if k==4:
        k=0
    turtle.forward(j)
    j=j-10
    turtle.left(90)

turtle.done()
