import turtle

wn= turtle.Screen()
tr =turtle.Turtle()

n=9
l=100

def ngon(n,l):
    ilosc_bokow=0
    kat=360/n
    while ilosc_bokow <n:
        tr.forward(l)
        tr.left(kat)
        ilosc_bokow=ilosc_bokow+1

def fxn(x,y):
    tr.goto(x,y)
    ngon(5,10)


wn.onclick(fxn)
wn.mainloop()
