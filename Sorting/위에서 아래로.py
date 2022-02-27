lst = [int(input()) for _ in range(int(input()))]
lst = sorted(lst, reverse=True)
for i in lst:
    print(i, end=' ')