# 4. Реализуйте базовый класс Car:
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

#################################################################################################

class Car:
    speed = 60
    color = 'black'
    name = 'Volvo'
    is_police = False
    def go(self):
        print("Машина поехла")
    def stop(self):
        print('Машина остановилась')
    def turn_to_the_left(self):
        print('Машина повернула налево')
    def turn_to_the_right(self):
        print('Машина повернула налево')
    def __init__(self, show_speed):
        self.show_speed = show_speed

class TownCar(Car):
    def __init__(self, show_speed):
        super().__init__(show_speed)
    def recomended_speed(self):
        if self.show_speed > Car.speed:
            print("Скорость превышена, ограничение по скорости 60 км/ч")
        else:
            print("Штраф не грозит")

t = TownCar(61)
print("Class TownCar")
print(f'Автомобиль {t.name}, цвет {t.color}, текущая скорость {t.show_speed} км/ч, полицейская? - {t.is_police}')
t.go()
t.recomended_speed()
t.turn_to_the_left()
t.turn_to_the_right()
t.stop()
print(sep='\n')

class SportCar(Car):
    max_speed = 250
print("Class SportCar")
s = SportCar(250)
s.show_speed = 160
s.name = 'Ferrari'
s.color = 'red'
print(f'Автомобиль {s.name}, цвет {s.color}, текущая скорость {s.show_speed} км/ч, максимальная скорость {s.max_speed} км/ч, полицейская? - {s.is_police}')
s.go()
s.turn_to_the_left()
s.turn_to_the_right()
s.stop()
print(sep='\n')

class WorkCar(Car):
    speed = 40
    def __init__(self, show_speed):
        super().__init__(show_speed)
    def recomended_speed(self):
        if self.show_speed > WorkCar.speed:
            print("Скорость превышена, ограничение скорости 40 км/ч")
        else:
            print("Штраф не грозит")

w = WorkCar(40)
print("Class WorkCar")
w.name = 'Renault'
w.color = 'grey'
print(f'Автомобиль {w.name}, цвет {w.color}, текущая скорость {w.show_speed} км/ч, полицейская? - {w.is_police}')
w.go()
w.recomended_speed()
w.turn_to_the_left()
w.turn_to_the_right()
w.stop()
print(sep='\n')

class PoliceCar(Car):
    is_police = True
print("Class PoliceCar")
p = PoliceCar(60)
p.show_speed = 60
p.name = 'Skoda'
p.color = 'white/black'
print(f'Автомобиль {p.name}, цвет {p.color}, текущая скорость {p.show_speed} км/ч, полицейская? - {p.is_police}')
p.go()
p.turn_to_the_left()
p.turn_to_the_right()
p.stop()
