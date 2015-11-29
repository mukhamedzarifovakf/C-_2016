import robot
r = robot.rmap()
r.lm('task9')
r.sleep = 0.005
def task():
    pass
    Square = 0
    while r.fu():
        r.up(1)
    while r.fr():
        r.rt(1)
    for i in range(0, 19,  1):
        for i in range(1, 19,  1):
            if r.cl():
                Square +=1
            r.lt(1)
        r.rt(18)
        if r.fd():
            r.dn(1)
    print(Square)