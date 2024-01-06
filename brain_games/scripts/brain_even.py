#!/usr/bin/env python3
from brain_games.games import even
from brain_games.engine import generate_round


def main():
    generate_round(even)


if __name__ == '__main__':
    main()
