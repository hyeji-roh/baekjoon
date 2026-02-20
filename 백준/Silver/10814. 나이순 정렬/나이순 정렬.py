N = int(input())
members = []

for _ in range(N):
    age, name = map(str, input().split())
    members.append((int(age), name))

for a, n in sorted(members, key=lambda x:x[0]):
    print(a, n)