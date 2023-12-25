#!/usr/bin/env python3
import random
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    print("What is the result of the expression?")
    for i in range(0,3):
        random_num = random.randint(1,100)
        random_num_2 = random.randint(1,100)
        operator = ['+','-', '*']
        random_operator = random.choice(operator)
        question = f"{random_num} {random_operator} {random_num_2}"
        print('Question:', question)
        answer = prompt.integer(f"Your answer: ")
        if answer != eval(question):
            return print(f"""{answer} is wrong answer ;(. Correct answer was {eval(question)}."
Let's try again, {name}!""")
        print("Correct!")
    return print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
