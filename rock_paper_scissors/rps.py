#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # define list of possible plays (rock, paper, scissors)
    options = ["rock", "paper", "scissors"]
    # tracker variable integer
    call_count = 0
    # empty list to append to
    possible_plays = [["rock"], ["paper"], ["scissors"]]

    updatedPlays = []

    if n == 0:
        return []
    elif n == 1:
        print(options)
        return options

    def handle_list(arr):
        # increment call count
        print("array", arr)
        nonlocal call_count
        call_count += 1
        for i in range(0, len(arr)):
            for j in range(0, len(options)):
                print(f"{options[j]}")
                banana = possible_plays[i] + [options[j]]
                print(f"possible plays: {possible_plays}")
                updatedPlays.append(banana)
                print(f"updatedPlays: {updatedPlays}")

        if call_count == n:
            return list
        else:
            handle_list(arr)

    handle_list(possible_plays)


rock_paper_scissors(3)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
