#!/usr/bin/env python3
from brain_games.games import gcd
from brain_games.engine import generate_round


def main():
    generate_round(gcd)


if __name__ == '__main__':
    main()
