#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # Recieves a list of stock prices as prices
    # return the maximum profit possible from a single buy and sell.
    # must first buy before selling
    pass


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
