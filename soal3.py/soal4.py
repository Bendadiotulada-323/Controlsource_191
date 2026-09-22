n = int(input("Masukan angka: "))

print(f"angka ganjil up to {n}:")
for i in range(1, n + 1, 2):
    print(i, end=" ")
print()