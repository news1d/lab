import random

a = int(input("Введите целое число: "))

ans_1 = a + random.randint(1, 100)
ans_2 = a * random.randint(1, 100)
ans_3 = a - random.randint(1, 100)
ans_4 = a / random.randint(1, 100)

print(ans_1, ans_2, ans_3, ans_4)

arr = [random.randint(1, 100) for i in range(a)]
print("Полученный массив:", arr)

