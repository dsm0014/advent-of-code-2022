from typing import List


def solve1(lines: List[str]) -> int:
    """
    num assignment pairs FULLY containing another
    """
    ans = 0
    for line in lines:
        s1, s2 = line.split(",")
        a, b = [int(i) for i in s1.split("-")]
        y, z = [int(i) for i in s2.split("-")]
        area1 = tuple(range(a, b+1))
        area2 = tuple(range(y, z+1))
        spread = set(area1 + area2)
        if len(spread) == len(area1) or len(spread) == len(area2):
            ans += 1

    return ans


def solve2(lines: List[str]) -> int:
    """
    num assignment pairs with ANY overlap
    """
    ans = 0
    for line in lines:
        s1, s2 = line.split(",")
        a, b = [int(i) for i in s1.split("-")]
        y, z = [int(i) for i in s2.split("-")]
        area1 = tuple(range(a, b+1))
        area2 = tuple(range(y, z+1))
        spread = set(area1 + area2)
        if len(spread) != len(area1) + len(area2):
            ans += 1

    return ans


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        linez = [line.strip() for line in f.readlines()]
    print(solve1(linez))
    print(solve2(linez))
