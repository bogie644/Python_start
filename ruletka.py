import turtle
import random
import math

import robot_helper


turtle.speed(0)
PHI = 360 / 7
R = 50
def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def draw_baraban(x, y):
    gotoxy(x, y)
    turtle.circle(80)
    gotoxy(x, y + 160)
    draw_circle(5, 'red')
    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(math.sin(phi_rad) * R + x, math.cos(phi_rad) * R + y + 60)
        draw_circle(21, 'white')


def draw_patron(x, y, start):
    for i in range(start, random.randrange(7, 100)):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(math.sin(phi_rad) * R + x, math.cos(phi_rad) * R + y +60)
        draw_circle(21, 'brown')
        draw_circle(21, 'white')
    gotoxy(math.sin(phi_rad) * R + x, math.cos(phi_rad) * R + y + 60)
    draw_circle(21, 'brown')
    return i % 7

x = 100
y = - 250
draw_baraban(x, y)
start = 0
answer = ''
while answer != 'N':
    answer = turtle.textinput('Поиграем?', 'ДА(Y)/НЕТ(N)')
    if answer == 'Y':

        start = draw_patron(x, y, start)
        start = 0
        if start == 0:
            gotoxy(-150, 250)
            turtle.write('Вы проиграли!', font=('Arial', 18, 'normal'))
            choice = turtle.textinput('Выбере наказание:', '1. Удаление случайного файла\n 2. Дублирование файлов')
            if choice == '1':
                robot_helper.del_random_file('.')
            elif choice == '2':
                robot_helper.duble_files('.')
            else:
                pass
    else:
        pass