import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(100)
h = 0
t.pensize(5)
def draw(angle, n):
    t.circle(5+n,60)
    t.left(angle)
    t.circle(5+n,60)
t.goto(0,0)
for i in range(250):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.008
    t.pencolor(c)
    draw(90,i*0.5)
    draw(160,i*1.2)
    t.penup()
    draw(180,i)
    draw(90,i*2)
    t.down()
t.done()