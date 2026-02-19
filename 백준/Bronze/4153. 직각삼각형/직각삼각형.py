while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    arr = [a, b, c]
    total = 0

    heru = max(arr)
    arr.remove(heru)

    for i in arr:
        total += i**2

    print("right" if total == heru**2 else "wrong")