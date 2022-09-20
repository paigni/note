import argparse
from note_class import Note

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', required=True)
    parser.add_argument('-s', required=True)
    parser.add_argument('-d', default=1, type=int)
    parser.add_argument('-e', default=1, type=int)
    parser.add_argument('-h', required=True)
    return parser


def create_new_note(notes):
    notes_headder = input('Введите заголовок заметки\n')
    notes_text = input('Введите текст заметки\n')
    notes.create_new_file(notes_header, notes_text)


note = Note()
create_new_note(note)

#if __name__ == '__main__':
    #note = Note()
    #parser = create_parser()
    #arg = parser.parse_args()
    #if arg == '-c':
        #create_new_note(note)

    #if arg == '-s':
        #note.read_note() # пока что,дальше будет цикл

    #if arg == '-d':
    #    del num
    #if arg == '-h':
        #faq


