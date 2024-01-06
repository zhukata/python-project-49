import random


GAME_RULES = """Answer "yes" if the number is even, otherwise answer "no"."""
MIN_NUM = 1
MAX_NUM = 100


def get_question():
    random_num = random.randint(MIN_NUM, MAX_NUM)
    question = random_num
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
