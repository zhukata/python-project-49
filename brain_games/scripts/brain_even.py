#!/usr/bin/env python3
import random
import prompt
from brain_games.even_game import check_answer


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    print("""Answer "yes" if the number is even, otherwise answer "no".""")
    for i in range(0,3):
        random_num = random.randint(1,100)
        print (f"Question: {random_num}")
        answer = prompt.string(f"Your answer: ")
        if check_answer(answer, random_num) == False:
            return print(f"""'yes' is wrong answer ;(. Correct answer was 'no'."
Let's try again, {name}!""")
        print("Correct!")
    return print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
