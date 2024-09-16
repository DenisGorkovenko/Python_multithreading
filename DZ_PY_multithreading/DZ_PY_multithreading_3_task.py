from threading import Thread
from random import randint


class ThreThread:

    def __init__(self):
        self.rnd_numbers = []
        self.average = 0
        self.summa = 0

    def rnd(self):
        self.rnd_numbers = [randint(0, 100) for i in range(10)]

    def summ(self):
        self.summa = sum(self.rnd_numbers)

    def avg(self):
        self.average = sum(self.rnd_numbers) / len(self.rnd_numbers)


thre_thread = ThreThread()

t1 = Thread(target=thre_thread.rnd())
t2 = Thread(target=thre_thread.summ())
t3 = Thread(target=thre_thread.avg())

t1.start()
t1.join()

t2.start()
t3.start()

print(*thre_thread.rnd_numbers, sep=', ')
print(f'Сумма {thre_thread.summa}')
print(f'Среднее арифметическое {thre_thread.average}')