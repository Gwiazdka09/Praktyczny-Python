# Program liczy liczby parzyste i nieparzyste w zakresie od 1 do 100

even_count = 0
odd_count = 0

for number in range(1, 101):
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Liczb parzystych: {even_count}")
print(f"Liczb nieparzystych: {odd_count}")
