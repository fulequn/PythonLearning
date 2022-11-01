# PythonDraw. py 
import turtle 
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)     #前景方向，bk后退方向
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)        #改变方向，不行进
for i in range(4):
    turtle.circle(40,80)        #以左侧某一点为圆心，做曲线运动
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()