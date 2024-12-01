with open("D1.txt") as f:
    data = f.read().splitlines()
    a, b = sorted([int(i.split()[0]) for i in data]), sorted([int(i.split()[1]) for i in data])
    print(sum([abs(a[i] - b[i]) for i in range(len(a))]))