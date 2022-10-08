#import turtle and random
from turtle import *
from random import randint
#color for bgcolor
list1=["blue","red","orange","green","purple"]
#color for pen
list2=["#663300","#00ffff","#4d0018","#933aff","#00ff3c"]
pensize(5)
for i in range(20):
    # create random number
    number1 = randint(0,4)
    number = randint(0,4)
    #set color
    color(list2[number1])
    bgcolor(list1[number])
    circle(100)
    left(360/20)
done()