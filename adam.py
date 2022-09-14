
"""
qwer="qwer"
print(qwer * 3)
def okej(): 
    k=input("HJHAHAHAHAHAHA")
    z=int(k)+69
    print(k,z,"beka")

okej()
okej()

pokemon=["emo","emoś","emil"]
for git in pokemon:
    print(git)
"""
from turtle import * 
from random import random

def gwiazda(kont, skok):
    hideturtle()
    bgcolor('#130428')
    width(1)
    speed(0)
    begin_fill()
    while True:
        r=random()
        g=random()
        b=random()
        pencolor(r,g,b)
        forward(skok)
        right(kont)
        if abs(pos()) < 1:
            break
gwiazda(170, 200)
end_fill()
penup()
goto(100,300)
write("Adam!!", font=("Arial",30,"normal"))
done()