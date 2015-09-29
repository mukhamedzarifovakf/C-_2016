#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.lm('task7')
r.sleep = 0.05
def task():
    pass
    while r.fr():
        r.rt(1)
    while r.fu():
        r.up(1)
    for i in range(0, 10, 1):
        for i in range(1,  15,  1):
            if r.wu() and r.wd():
                r.lt(1)
                if r.wu() and r.wd():
                    r.pt()
                    r.rt(1)
                    r.pt()
                else:
                    r.rt(1)
            r.lt(1)
        r.rt(14)
        r.dn()
	
	#------- пишите код здесь -----
r.start(task)

#Отступ слева (tab) сохранять!
#r.help() - Список команд и краткие примеры
#r.demo() - показать решение этой задачи (только результат, не текст программы)
#r.demoAll() - показать все задачи (примерно 20 минут)

#r.rt() - вправо
#r.rt(3)- вправо на 3
#r.dn() - вниз
#r.up() - вверх
#r.lt() - влево
#r.pt() - закрасить  Paint

#r.cl() - закрашена ли клетка? Color
#r.fr() - свободно ли справа? freeRight
#r.fl() - свободно ли слева?  freeLeft
#r.fu() - свободно ли сверху? freeUp
#r.fd() - свободно ли снизу?  freeDown

#r.wr() - стена ли справа? freeRight
#r.wl() - стена ли слева?  freeLeft
#r.wu() - стена ли сверху? freeUp
#r.wd() - стена ли снизу?  freeDown


#red - красный
#blue - синий
#yellow - желтый
#green - зеленый
