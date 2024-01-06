#!/usr/bin/env python3
from brain_games.games import calc
from brain_games.engine import generate_round


def main():
    generate_round(calc)


if __name__ == '__main__':
    main()
