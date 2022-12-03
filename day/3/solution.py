import string


def solve1(file) -> int:
    """
    bag split compartments grand total
    """
    ans = 0
    for line in file.readlines():
        mid = int(len(line) / 2)
        c1, c2 = line[:mid], line[mid:]
        ans += next(string.ascii_uppercase.index(i) + 27 if i not in string.ascii_lowercase
                    else string.ascii_lowercase.index(i) + 1 for i in c1 if i in c2)
    return ans


def solve2(file) -> int:
    """
    common in compartments per 3 elves
    """
    ans = 0
    l = file.readlines()
    for i, line in enumerate(l):
        if i % 3:
            continue
        ans += next(string.ascii_uppercase.index(j) + 27 if j not in string.ascii_lowercase
                    else string.ascii_lowercase.index(j) + 1 for j in line if j in l[i + 1] and j in l[i + 2])

    return ans


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        print(solve1(f))

    with open('data.txt', 'r') as f:
        print(solve2(f))
