a = [5, 3, 2, 8, 1, 4]
print(a)
b = sorted([item for item in a if item%2 == 0])
odd_int = 0
for i in range(len(a)):
    print("a: ", a)
    if a[i] %2 == 0:
        print("b: ", b)
        a[i] = b[odd_int]
        odd_int += 1

print(b)
print(a)