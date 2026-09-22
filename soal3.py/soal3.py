n = int(input("Masukanlah nilai n (number of terms): "))

a = 0
b = 1

print("Deret Fibonanci:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()