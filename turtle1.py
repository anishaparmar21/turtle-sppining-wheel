import turtle
a=turtle.Turtle()
list1=["purple","red","orange","blue","green"]
for i in range(200):
    a.color(list1[i%5])
    a.pensize(i%10+1)
    a.forword(i)
    a.left(60)
    
