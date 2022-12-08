from typing import List


def solve1(lines: List[str]) -> int:
    """
    find start of packet (first unique 4 chars)
    """
    for line in lines:
        for i, c in enumerate(line):
            if i < 3:
                continue
            a = 3
            tmp = {c}
            while a > 0:
                tmp.add(line[i-a])
                a -= 1
            if len(tmp) == 4:
                print(tmp)
                return i + 1


def solve2(lines: List[str]) -> int:
    """
    find start of msg (first unique 14 chars)
    """
    for line in lines:
        for i, c in enumerate(line):
            if i < 13:
                continue
            a = 13
            tmp = {c}
            while a > 0:
                tmp.add(line[i-a])
                a -= 1
            if len(tmp) == 14:
                return i + 1


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        linez = [line.strip() for line in f.readlines()]
    print(solve1(linez))
    print(solve2(linez))
