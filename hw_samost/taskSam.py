# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
#  причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
# на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.


gardenBed = int(input("number of bushes :  "))
berryBush = []
i = 0
for i in range(gardenBed):
    berryBush.append(int(input("berry : ")))
print(berryBush)
# Создал массив. заполним массив . и все . далее(что ниже ) вообще не понял. надо разобраться !!!!

berryCount = list()
for i in range(len(berryBush) - 1 ):
    berryCount.append(berryBush[i-1] + berryBush[i] + berryBush[i+1])
berryCount.append(berryBush[-2] + berryBush[-1] + berryBush[0])
print(max(berryCount))

# # разобрался . но все же сложновато для понимания. по крайней мере сразу. 