n = int(input())
lst = []
for i in range(n):
    data = input().split()
    lst.append((data[0], int(data[1])))

lst = sorted(lst, key=lambda x:x[1])
for i in lst:
    print(i[0], end=' ')