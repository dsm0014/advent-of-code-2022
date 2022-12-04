from enum import Enum


class Hand(Enum):
    ROCK = {"guide": ["A", "X"], "score": 1}
    PAPER = {"guide": ["B", "Y"], "score": 2}
    SCISSORS = {"guide": ["C", "Z"], "score": 3}

    @classmethod
    def fromGuide(cls, hand):
        if hand in cls.ROCK.value["guide"]:
            return Hand.ROCK
        elif hand in cls.PAPER.value["guide"]:
            return Hand.PAPER
        else:
            return Hand.SCISSORS

    @classmethod
    def winsAgainst(cls, opp):
        if opp == cls.ROCK:
            return cls.PAPER
        elif opp == cls.PAPER:
            return cls.SCISSORS
        return cls.ROCK

    @classmethod
    def losesAgainst(cls, opp):
        if opp == cls.ROCK:
            return cls.SCISSORS
        elif opp == cls.PAPER:
            return cls.ROCK
        return cls.PAPER

#    0 always draw
#    1 win paper vs rock
#    -1 loss paper vs scissors
#    1 win scissors vs paper
#    2 loss scissors vs rock
#    2 win rock vs scissors
#    -1 loss rock vs paper
#    -2 loss rock vs scissors
def scoreHands(i, you):
    ans = 0
    res = i.value["score"] - you.value["score"]
    if res == -2 or 0 < res < 2:
        ans += 6
    elif res == 0:
        ans += 3
    return ans + i.value["score"]

def solve1(file) -> int:
    """
    tally Rock Paper Scissors score by following the guide
    """
    ans = 0
    for line in file.readlines():
        you, i = [Hand.fromGuide(j) for j in line.strip().split(" ")]
        ans += scoreHands(i, you)
    return ans


def solve2(file) -> int:
    """
    tally Rock Paper Scissors score by producing compliments to the opponent
    """
    ans = 0
    for line in file.readlines():
        you, i = line.strip().split(" ")
        you = Hand.fromGuide(you)
        if i == "Z":
            i = Hand.winsAgainst(you)
        elif i == "X":
            i = Hand.losesAgainst(you)
        else:
            i = you
        ans += scoreHands(i, you)

    return ans




if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        print(solve1(f))

    with open('data.txt', 'r') as f:
        print(solve2(f))
