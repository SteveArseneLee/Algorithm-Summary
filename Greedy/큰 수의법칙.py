# N,M,K = map(int, input().rstrip().split())
# lst = list(map(int, input().split()))
# lst.sort()
# first = lst[-1]
# second = lst[-2]
# result = 0
# while True:
#     for i in range(K):
#         if M == 0:
#             break
#         result += first
#         M -= 1
#     if M == 0:
#         break
#     result += second
#     M -= 1
# print(result)

# ----------------------------------------
N,M,K = map(int, input().rstrip().split())
lst = list(map(int, input().split()))
lst.sort()
first = lst[-1]
second = lst[-2]

count = int(M / (K+1)) * K
count += M % (K+1)

result = 0
result += (count)*first # 가장 큰 수 더하기
result += (M-count) * second # 두 번째로 큰 수 더하기
print(result)