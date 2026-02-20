N = int(input())
arr = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

for answer in sorted(arr, key=lambda x:(x[0], x[1])):
    print(answer[0], answer[1])