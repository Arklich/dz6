x = int(input())
z = 0
for i in range(1, x + 1):
    if x % i == 0:
        z = z + 1
print(z)