import math
import turtle
from turtle import*
def haerta(k):
    return 15*math.sin(k)**3
def heartb(K):
    return 12*math.cos(K)-5*\
    math.cos(2*K)-2*\
                     math.cos(3*K)-\
                     math.cos(4*K)
speed(0)
bgcolor("black")
for i in range(1000):
    goto(haerta(i)*20,heartb(i)*20)
    for j in range(5):
        color("#f73487")
        goto(0,0)
done()
