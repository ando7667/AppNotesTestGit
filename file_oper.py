import os
import random
import logger as lg

file = ['notes.csv', 'history.log']

file_head = [
    'id_note;title;content;date_create;date_edit\n',
    ''
]


def search_max_id():
    if check_file(file[0]):
        with open(file[0], 'r', encoding='utf-8') as f1:
            # пропускаем строку заголовков полей
            line = f1.readline()
            # читаем заметки
            lines = f1.readlines()
            idmax = 0
            index = 0
            for line in lines:
                index += 1
                idi = int(line.strip('\n').split(";")[0])
                if idi > idmax: idmax = idi
            return idmax, index


def search_index_rec(ids):
    try:
        with open(file[0], 'r', encoding='utf-8') as f1:
            # пропускаем строку заголовков полей
            line = f1.readline()
            # читаем заметки
            lines = f1.readlines()
            index = 1
            for line in lines:
                index += 1
                st = line.strip('\n').split(";")[0]
                if st == ids:
                    return index
    except:
        print("ошибка с файлом")


def check_file(f1: str):
    if os.access(f1, os.F_OK):
        return True
    else:
        return False


def writing_scv(rec: list, fl: str):
    if check_file(fl):
        with open(fl, 'a', encoding='utf-8') as f1:
            rec.insert(0, search_max_id()[0] + 1)
            f1.write(f'{rec[0]};{rec[1]};{rec[2]};{rec[3]};{rec[4]}\n')
            lg.logger_history("Запись новой заметки", f"{rec[0]} {rec[1]} {rec[3]}", "удачно")
    else:
        print(f"файл {fl} не найден!")
        lg.logger_history("Новая заметка не сохранен", f"{rec[0]} {rec[1]} {rec[3]}", "Файл не найден")


def creat_file():
    for i, f in enumerate(file):
        if not check_file(f):
            with open(f, 'w', encoding='utf-8') as f1:
                f1.write(file_head[i])
                lg.logger_history("Создан отсутствующий файл ", f"{f}", "")


def read_scv(fl: str):
    if check_file(fl):
        with open(fl, 'r', encoding='utf-8') as f1:
            return f1.readlines()
    else:
        print(f"файл {fl} не найден!")
        lg.logger_history("Ошибка чтения файла", f"{fl}", "не найден")
        return []


def read_rec_csv(fl: str, ids):
    if check_file(fl):
        with open(fl, 'r', encoding='utf-8') as f1:
            lines = f1.readlines()
            for line in lines:
                st = line.strip('\n').split(";")
                if st[0] == ids:
                    return st
    else:
        print(f"файл {fl} не найден!")
        lg.logger_history("Ошибка чтения файла", f"{fl}", "не найден")
        return []


def delete_rec_in_file(ids):
    try:
        with open('notes.csv', 'r', encoding='utf-8') as fr:
            lines = fr.readlines()

            with open('notes.csv', 'w', encoding='utf-8') as fw:
                for line in lines:
                    st = line.strip('\n').split(";")[0]
                    if st != ids:
                        fw.write(line)
                    else:
                        lg.logger_history("Удаление записи", f"id={st}", "Успешно!")
                        return st
    except:
        print("Ошибочка!")
