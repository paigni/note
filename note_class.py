import json
import datetime
import os.path
import sys

from check import check_list, check_note_number


class Note:
    __header = ''
    __text = ''
    __time_update = ''
    __time_create = ''

    def now(self):
        """
            Метод печатает текущую дату и время

            Returns:
                Текущую дату и время
            """
        now = datetime.datetime.now()
        return now.strftime("%d-%m-%Y %H:%M")

    def read_note(self):
        """
            Метод проверяет существования файла,
            если файл существует, возвращает список.
            Если не существует, создаёт список и возвращает его

            Returns:
                ввод пользователя
            """
        check_file = os.path.exists('notes.json')
        if not check_file:
            data = []
            self.save_changes(data)
        else:
            with open('notes.json', 'r') as write_file:
                data = json.load(write_file)
        return data

    def save_changes(self, data):
        """
            Метод сохраняет изменения в файле
        """
        with open('notes.json', 'w') as write_file:
            json.dump(data, write_file)

    def show_notes(self):
        """
            Метод показывает все заметки оставленные пользователем
        """
        count = 0
        notes = self.read_note()
        if not check_list(notes):
            print("Заголовок    Текст   Время создания    Время обновления")
            for note in notes:
                count += 1
                print(
                    f"{count}){note['header']} {note['text']}"
                    f" {note['time_create']} {note['time_update']}"
                )
        else:
            sys.exit("Заметок не найдено")

    def action_with_note(self, header: str, text: str, count: int = -1):
        """
        Метод создаёт новую заметку если count = -1
        В случае если пользователь указал count метод редактирует указанную заметку
        Args:
            header: Заголовок заметки
            text: Текст заметки
            count: номер заметки
        """
        data = self.read_note()
        self.__text = text
        self.__header = header
        self.__time_update = self.now()
        if count == -1:
            note = {
                'header': self.__header,
                'text': self.__text,
                'time_create': self.now(),
                'time_update': self.__time_update
            }
            data.append(note)
            self.save_changes(data)
        else:
            if not check_list(data):
                time_cr = data[count - 1].get('time_create')
                note = {
                    'header': self.__header,
                    'text': self.__text,
                    'time_create': time_cr,
                    'time_update': self.__time_update
                }
                data[count - 1].update(note)
                self.save_changes(data)
            else:
                sys.exit("Нельзя редактировать заметки которой не существует")

    def delete_note(self, user_inp: int):
        """
        Метод удаляет заметку указанную пользователем
        Args:
            user_inp: номер заметки указанной пользователем
        """
        data = self.read_note()
        if not check_list(data):
            data.pop(user_inp - 1)
            self.save_changes(data)
        else:
            sys.exit("Для удаления заметки,добавьте её в список")
