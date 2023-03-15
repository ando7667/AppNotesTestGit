import actions


class Menu:
    _action = None
    _arr_action = []

    def __init__(self):
        self._action = 0

        self._arr_action = {
            0: "Выход",
            1: "Создать заметку",
            2: "Изменить заметку",
            3: "Удалить заметку",
            4: "Посмотреть заметку",
            5: "Посмотреть заметки по заголовку",
            6: "Посмотреть заметки по дате",
            7: "Посмотреть все заметки",
            8: "Посмотреть наибольший ИД в записях"
        }

    def get_action(self):
        return self._action

    def get_arr_action(self):
        return self._arr_action

    def strin_rep(self, st: str):
        st = st.replace("-", "").replace(",", ".").split(".")[0]
        return st

    def show_text(self, arr):
        for key, value in arr.items():
            print(f"{key} - {value}")

    def get_number(self):
        inp = self.strin_rep(input())
        if inp.isdigit() and int(inp) >= 0:
            return int(inp)

    def set_action(self):
        while True:
            print("Выберите действие:\n")
            self.show_text(self._arr_action)
            self._action = self.get_number()
            if 0 <= self._action < len(self._arr_action):
                break

    def show_menu(self):
        while True:
            self.set_action()
            if self._action == 0:
                exit("До свидания!")
            elif self._action == 1:
                actions.add_note()
            elif self._action == 2:
                actions.edit_note()
            elif self._action == 3:
                actions.delete_note()
            elif self._action == 4:
                actions.view_note()
            elif self._action == 5:
                actions.view_search_title()
            elif self._action == 6:
                actions.view_search_data()
            elif self._action == 7:
                actions.view_all_notes()
            elif self._action == 8:
                actions.view_max_id()
