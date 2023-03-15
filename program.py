import menu as mn
import file_oper as fo

if __name__ == '__main__':
    print("Программа работы с Заметками")
    fo.creat_file()
    m = mn.Menu()
    m.show_menu()
