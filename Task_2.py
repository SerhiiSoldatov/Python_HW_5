# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом"

import random

def examination(a,player,n):
    i=1
    while i==1:
        if a<1 or a>28:
            print(f'Взято не верное количество конфет {a}')
            a=int(input(f'Игрок {player}. Возьмите со стола от 1 до 28 конфет: '))
        elif a>n:
            print(f'Взято не верное количество конфет {a} больше оставшихся на столе {n}')
            a=int(input(f'Игрок {player}. Возьмите со стола от 1 до 28 конфет: '))
        else: i+=1
    return a

i=1
while i==1:
    mode=int(input('1.Человек с человеком - 1\n2.Человек с ботом - 2\nВыберите режим игры:'))
    if mode<1 or mode>2:
        print(f'Вы ввели неправильное значение {mode}')
    else: i+=1

if mode==2:
    i=1    
    while i==1:
        variant=int(input('1.Бот без интелекта - 1\n2.Бот с интелектом - 2\nВыберите вариант бота:'))
        if variant<1 or variant>2:
            print(f'Вы ввели неправильное значение {variant}')
        else: i+=1

print('Игра началась!')
n=2021
if random.randint(1,3)==1:
    if mode==2:
        print('Игру начинает человек')
        player1='человек' 
        player2='бот'
    else:
        player1='номер 1' 
        player2='номер 2' 
        print('Игру начинает игрок под номером 1')
    
else:
    if mode==2:
        print('Игру начинает бот')
        player1='бот' 
        player2='человек'
    else:
        player1='номер 2' 
        player2='номер 1' 
        print('Игру начинает игрок под номером 2')

while n!=0:
    print(f'На столе лежит {n} штук конфет')
    if n<28:
        m=n
    else:
        m=28
    if player1=='бот':
        if variant==1:
            move1=random.randint(1,m)            
        else:
            if n%29!=0:
                move1=n%29
            else:
                move1=random.randint(1,m)
        print(f'бот взял {move1} штук конфет')        
    else:
        move1=int(input(f'Игрок {player1}. Возьмите со стола от 1 до {m} конфет: '))
    move1=examination(move1,player1,n)
    n-=move1    
    if n==0:
        print(f'Конфет на столе не осталось. Игрок {player1} победил!')
        break
    else:
        print(f'На столе осталось {n} штук конфет')
    if n<28:
        m=n
    else:
        m=28
    if player2=='бот':
        if variant==1:
            move2=random.randint(1,m)
        else:
            if n%29!=0:
                move2=n%29                
            else:
                move2=random.randint(1,m)
        print(f'бот взял {move2} штук конфет')
    else:
        move2=int(input(f'Игрок {player2}. Возьмите со стола от 1 до {m} конфет: '))
    move2=examination(move2,player2,n)
    n-=move2    
    if n==0:
        print(f'Конфет на столе не осталось. Игрок {player2} победил!')
    else:
        print(f'На столе осталось {n} штук конфет')
