#Дано целое число N (>0). Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей)
try:
    n = int(input("Введите целое число N (>0): "))
except ValueError:
    print("Ошибка: введите целое число")
    exit()

if n <= 0:
    print("Ошибка: N должно быть больше 0")
else:
    product = 1.0
    current = 1.1
    for i in range(n):
        product *= current
        current += 0.1

    print(f"Произведение {n} сомножителей: {product}")