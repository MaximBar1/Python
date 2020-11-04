a = input('строка : ')
x = len(a) + 1
part_1 = a[0:x//2]
part_2 = a[x//2:]
if part_1[-1] == part_1[0]:
    print(a)
else:
    print(part_1[-1])