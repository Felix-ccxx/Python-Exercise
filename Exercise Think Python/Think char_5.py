def draw(t,length,n):
    if n==0:
        #print('return',n)
        return
    angle=50
    t.fd(length*n)
    t.lt(angle)
    #print ('first ',n)
    draw(t,length,n-1)
    t.rt(2*angle)
    #print ('second ',n)
    draw(t,length,n-1)
    t.lt(angle)
    t.bk(length*n)


def koch(t, n):
    """Draws a koch curve with length n."""
    if n<3:
        fd(t, n)
        return
    m = n/3.0
    koch(t, m)
    lt(t, 60)
    koch(t, m)
    rt(t, 120)
    koch(t, m)
    lt(t, 60)
    koch(t, m)

def fd(t,n):
    t.fd(n)

def lt(t,angle):
    t.lt(angle)

def rt(t,angle):
    t.rt(angle)

def snowflake(t,length):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""

    for i in range(3):
        koch(t,length)
        rt(t,120)

