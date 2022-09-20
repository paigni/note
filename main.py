import argparse
import sys

from note_class import Note


def create_parser():
    parser = argparse.ArgumentParser(prog = 'Заметки',
            description = '''Это очень полезная программа,
                            которая позволяет создавать,смотреть 
                            и обновлять заметки.''',
            epilog = '''-c – начало создание новой заметки
                        -s - показ списка заметок
                        -d<num>- удалить заметку под номером num
                        -e<num>- изменить заметку под номером num
                        -h- вывод справки об использовании'''
            )
    parser.add_argument('-c', required=True)
    parser.add_argument('-s', required=True)
    parser.add_argument('-d', default=1, type=int)
    parser.add_argument('-e', default=1, type=int)
    return parser


def action_with_note():
    note = Note()
    parser = create_parser()
    argum = parser.parse_args(sys.argv[1:])

    if argum == '-c':
        notes_header = input('Введите заголовок заметки\n')
        notes_text = input('Введите текст заметки\n')
        note.create_new_note(notes_header, notes_text)

    elif argum == '-s':
        note.read_note()

    elif argum == '-d':
        note.delete_note(argum.d)

    elif argum == '-e':
        notes_header = input('Введите заголовок заметки\n')
        notes_text = input('Введите текст заметки\n')
        note.change_note(notes_header, notes_text, argum.e)

action_with_note()