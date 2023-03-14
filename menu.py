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
            5: "Посмотреть все заметки"
        }

    def getAction(self):
        return self._action

    def getArrAction(self):
        return self._arr_action

    def strin_rep(self, st: str):
        st = st.replace("-", "").replace(",", ".").split(".")[0]
        return st

    def showText(self, arr):
        for key, value in arr.items():
            print(f"{key} - {value}")

    def getNumber(self):
        inp = self.strin_rep(input())
        if inp.isdigit() and int(inp) >= 0:
            return int(inp)

    def setAction(self):
        while True:
            print("Выберите операцию:\n")
            self.showText(self._arr_action)
            self._action = self.getNumber()
            if 0 <= self._action < len(self._arr_action):
                break

    def showMenu(self):
        self.setAction()


