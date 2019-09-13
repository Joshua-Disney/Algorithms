#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # define list of possible plays (rock, paper, scissors)
    options = ["rock", "paper", "scissors"]
    # list that gets returned
    updatedPlays = []

    def recursiveHelp(count, list=[]):
        if count > 0:
            for i in options:
                temp = list + [i]
                recursiveHelp(count - 1, temp)
        else:
            updatedPlays.append(list)
    recursiveHelp(n)
    print(updatedPlays)
    return updatedPlays


rock_paper_scissors(3)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
