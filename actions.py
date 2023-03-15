import file_oper as fo
from datetime import datetime as dtime
import menu as m
import logger as lg

file = fo.file[0]


def input_data():
    data_rec = []
    title = input('Введите Заголовок: ')
    data_rec.append(title)
    content = input('Введите Содержание: ')
    data_rec.append(content)
    tm = dtime.now().strftime('%d.%m.%y %H:%M')
    data_rec.append(tm)
    data_rec.append(tm)

    return data_rec


def add_note():
    rec = input_data()
    print(rec)
    fo.writing_scv(rec, file)
    return 1


def edit_note():
    idd = input('Введите id заметки для Редактирования: ')

    fo.delete_rec_in_file(idd)

    print("Запись сохранена!")
    return 1


def delete_note():
    idd = input('Введите id заметки для Удаления: ')
    iddok = fo.delete_rec_in_file(idd)
    print(f"Запись {iddok} удалена!")
    return 1


def view_note():
    idr = input('Введите id заметки для Просмотра: ')
    rec = fo.read_rec_csv(file, idr)
    print(rec)
    return 1


def view_search_title():
    work = fo.read_scv(file)
    title = input('Введите заголовок: ')
    for line in work:
        st = line.strip('\n').split(";")
        if title in st[1]:
            print(st)
    return 1


def view_search_data():
    date = input('Введите Дату (дд.мм.гг): ')
    print(f"Заметки на дату: {date} \n"
          f"{'=' * 30}")
    wk = []
    work = fo.read_scv(file)
    for w in work:
        wk = w.replace("\n", "").split(";")
        if wk[3].split(" ")[0] == date:
            print(wk)
    print(f"{'-' * 30}")
    lg.logger_history("Вывод заметок на дату ", f"{date}", "")
    return 1


def view_all_notes():
    print("Все заметки\n"
          f"{'=' * 30}")
    wk = []
    work = fo.read_scv(file)
    for w in work:
        wk = w.replace("\n", "").split(";")
        print(wk)
    print(f"{'-' * 30}")
    lg.logger_history("Вывод всех заметок", "", "")
    return 1

def view_max_id():
    print(f"max_id={fo.search_max_id()}")
    fo.search_max_id()
    return 1
