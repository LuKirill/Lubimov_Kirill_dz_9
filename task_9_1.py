# 1. Создать класс TrafficLight (светофор):
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.

#######################################################################################################################

from time import sleep
from random import shuffle
from sys import exit

class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        copy_color = TrafficLight.__color[:]
        while True:
            for i in range(3):
                if copy_color[i] != TrafficLight.__color[i]:
                    print('The TrafficLight is broken')
                    exit()
                elif copy_color[i] == 'red':
                    sleep(7)
                elif copy_color[i] == 'yellow':
                    sleep(2)
                elif copy_color[i] == 'green':
                    sleep(1)
                print(f'{copy_color[i]}')
            shuffle(copy_color)
a = TrafficLight()
a.running()