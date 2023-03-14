# программа работы с заметками

 #   from input import input_data as inpd
 #   import action as a
import menu

if __name__ == '__main__':
 #   action_list = [a.Calculator.sum, a.Calculator.sub, a.Calculator.mult, a.Calculator.div, a.Calculator.pow,
#                   a.Calculator.div_compl, a.Calculator.remainder_div, a.Calculator.sqrt_pow]
    print("Программа Калькулятор")
    m = menu.Menu()
#    calc = a.Calculator()
    while True:
        m.showMenu()
        if m.getAction() == 0:
            print("Пока!")
            break
        else:
            print("Работаем!")

