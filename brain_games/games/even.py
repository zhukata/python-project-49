import random


game_rules = """Answer "yes" if the number is even, otherwise answer "no"."""


def question_func():
    random_num = random.randint(1, 100)
    question = random_num
    return question


def correct_answer(question):
    if question % 2 == 0:
        correct_answer = 'yes'
        return correct_answer
    correct_answer = 'no'
    return correct_answer
