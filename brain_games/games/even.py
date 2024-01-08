import random


GAME_RULES = """Answer "yes" if the number is even, otherwise answer "no"."""
MIN_NUM = 1
MAX_NUM = 100


def get_question():
    """Generates a random question and returns it and the correct answer."""
    random_num = random.randint(MIN_NUM, MAX_NUM)
    question = random_num
    correct_answer = isEven(question)
    return question, correct_answer


def isEven(question):
    """Checks if the number is even."""
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
