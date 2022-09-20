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
        for note in data:
            print(note)

    def save_changes(self, data):
        with open('notes.json', 'w') as write_file:
            json.dump(data, write_file)


    def action_over_note(self, header, text):
        with open('notes.json', 'r') as write_file:
            data = json.load(write_file)

        self.__text = text
        self.__header = header
        if self.__time_create == '':
            self.__time_create = self.now()
            self.__time_update = ''
        else:
            self.__time_update = self.now()

        note = {
            'header': self.__header,
            'text': self.__text,
            'time_create': self.now(),
            'time_update': self.__time_update
        }
        data.append(note)
        self.save_changes(data)

    def create_new_file(self,header,text):
        check_file = os.path.exists('notes.json')
        if not check_file:
            data = []
            self.save_changes(data)
            self.action_over_note(header, text)
        else:
            self.action_over_note(header,text)

