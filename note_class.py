import json
import datetime
import os.path


class Note:
    __header = ''
    __text = ''
    __time_update = ''
    __time_create = ''

    def now(self):
        now = datetime.datetime.now()
        return now.strftime("%d-%m-%Y %H:%M")

    def read_note(self):
        with open('notes.json', 'r') as write_file:
            data = json.load(write_file)
            return data

    def save_changes(self, data):
        with open('notes.json', 'w') as write_file:
            json.dump(data, write_file)

    def show_notes(self):
        count = 0
        for note in self.read_note():
            count += 1
            print(f"{count}){note['header']} {note['text']} {note['time_create']} {note['time_update']}")

    def create_new_note(self, header, text):
        check_file = os.path.exists('notes.json')
        if not check_file:
            data = []
            self.save_changes(data)
        data = self.read_note()
        self.__text = text
        self.__header = header
        self.__time_create = self.now()
        self.__time_update = ''
        note = {
            'header': self.__header,
            'text': self.__text,
            'time_create': self.now(),
            'time_update': self.__time_update
        }
        data.append(note)
        self.save_changes(data)

    def change_note(self, header, text, count):
        data = self.read_note()[count]
        self.__text = text
        self.__header = header
        self.__time_create = self.__time_create
        self.__time_update = self.now()
        note = {
            'header': self.__header,
            'text': self.__text,
            'time_create': self.now(),
            'time_update': self.__time_update
        }
        data.append(note)
        self.save_changes(data)

    def delete_note(self, user_inp):
        data = self.read_note()
        data.pop(user_inp)
