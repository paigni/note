import argparse
from note_class import Note
from check import check_correct_inp
import sys


def create_parser():
    """
    Парсер служит для создания аргументов командной строки
    """
    pars = argparse.ArgumentParser(
        prog='Заметки',
        description='''Это очень полезная программа,
                       которая позволяет создавать,смотреть 
                       и обновлять заметки.''',
        epilog='''-c – начало создание новой заметки
                  -s - показ списка заметок
                  -d<num>- удалить заметку под номером num
                  -e<num>- изменить заметку под номером num
                  -h- вывод справки об использовании'''
                                   )
    my_group = pars.add_mutually_exclusive_group(required=True)
    my_group.add_argument('-c', action='store_true')
    my_group.add_argument('-s', action='store_true')
    my_group.add_argument('-d', action='store', nargs=1, type=int)
    my_group.add_argument('-e', action='store', nargs=1, type=int)
    return pars


def main():
    """
    Основная функция которая в зависимости от аргумента пользователя
    Принимает решение, что дальше делать
    """
    note = Note()
    parser = create_parser()
    argum = parser.parse_args()

    if argum.c:
        notes_header = input('Введите заголовок заметки\n')
        notes_text = input('Введите текст заметки\n')
        note.action_with_note(notes_header, notes_text)

    if argum.s:
        note.show_notes()

    if argum.d:
        if check_correct_inp(argum.d[0]):
            note.delete_note(argum.d[0])
        else:
            sys.exit('Передаваемое число должно быть больше 0 целочисленным и больше 0')

    if argum.e:
        if check_correct_inp(argum.e[0]):
            notes_header = input('Введите заголовок заметки\n')
            notes_text = input('Введите текст заметки\n')
            note.action_with_note(notes_header, notes_text, argum.e[0])
        else:
            sys.exit('Передаваемое число должно быть больше 0 целочисленным и больше 0')


if __name__ == '__main__':
    main()
