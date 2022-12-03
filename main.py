number = input()

suma = 0
mult = 1

for digit in number:
    suma += int(digit)
    mult += int(digit)

print("Сумма:", suma)