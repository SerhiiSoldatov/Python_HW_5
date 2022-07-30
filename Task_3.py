# Создайте программу для игры в ""Крестики-нолики"".

def examinationWin(field):
    if field[:5]=='X X X' or\
        field[6:11]=='X X X' or\
        field[12:17]=='X X X' or\
        field[::6]=='XXX' or\
        field[2::6]=='XXX' or\
        field[4::6]=='XXX' or\
        field[::8]=='XXX' or\
        field[4:13:4]=='XXX':
        print('Х победили!')
        return 'X'
    elif field[:5]=='O O O' or\
        field[6:11]=='O O O' or\
        field[12:17]=='O O O' or\
        field[::6]=='OOO' or\
        field[2::6]=='OOO' or\
        field[4::6]=='OOO' or\
        field[::8]=='OOO' or\
        field[4:13:4]=='OOO':
        print('O победили!')
        return 'O'
    else:
        return
        
field='1 2 3 4 5 6 7 8 9'
print(field[:5])
print(field[6:11])
print(field[12:17])

for i in range(1,6):
    i=1
    while i==1:
        x=str(input('Введите номер, на место которого поставить Х:'))
        if x in field:
            field=field.replace(x,'X')
            i+=1
        else:
            print('Место занято')
    print(field[:5])
    print(field[6:11])
    print(field[12:17])
    if examinationWin(field):break
    if '1'and'2'and'3'and'4'and'5'and'6'and'7'and'8'and'9' not in field:
        print('Ничья')
        break
    i=1
    while i==1:
        o=str(input('Введите номер, на место которого поставить O:'))
        if o in field:
            field=field.replace(o,'O')
            i+=1
        else:
            print('Место занято')
    print(field[:5])
    print(field[6:11])
    print(field[12:17])
    if examinationWin(field):break
    if '1'and'2'and'3'and'4'and'5'and'6'and'7'and'8'and'9' not in field:
        print('Ничья')
        break