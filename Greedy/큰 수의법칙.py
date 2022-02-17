N,M,K = map(int, input().rstrip().split())
lst = list(map(int, input().split()))
lst.sort()
first = lst[-1]
second = lst[-2]
result = 0
while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1
print(result)