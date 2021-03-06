# 5. Реализовать класс Stationery (канцелярская принадлежность):
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

###########################################################################################

class Stationery:
    title = "Канцелярская принадлежность"
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw1(self):
        print('карандашом')

p = Pen()
p.draw()
p.draw1()
print(sep='\n')

class Pensil(Stationery):
    def draw2(self):
        print('ручкой')

p = Pensil()
p.draw()
p.draw2()
print(sep='\n')

class Handle(Stationery):
    def draw3(self):
        print('маркером')

p = Handle()
p.draw()
p.draw3()
print(sep='\n')