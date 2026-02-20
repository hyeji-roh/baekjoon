N = int(input())
tmp = 1
result = []
count = 0

for i in range(N, 1, -1):
    tmp *= i

for n in str(tmp):
    result.append(n)

result = result[::-1]

for c in result:
    if c != '0':
        print(count)
        break
    else :
        count += 1