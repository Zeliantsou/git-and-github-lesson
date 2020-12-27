a = float(input("введиет значение a: "))
b = float(input("введиет значение b: "))
c = float(input("введиет значение c: "))
print((a and b and c and "Нет нулевых значений!!!") or "Есть нулевые значения")
print("Первое ненулевое значение:", (a or b or c) or (a or b or c or "Введены все нули!"))
if a > (b + c):
    print("a - b - c =", a - b - c)
elif a < (b + c): 
    print("b + c - a =", b + c - a)
if a > 50 and (b > a or c > a):
    print("Вася")
if a > 5 or (b == 7 and c == 7):
    print("Петя")
input()