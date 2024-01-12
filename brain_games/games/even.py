import random


GAME_RULES = """Answer "yes" if the number is even, otherwise answer "no"."""
MIN_NUM = 1
MAX_NUM = 100


def generate_round():
    """Generates a random question and returns it and the correct answer."""
    random_num = random.randint(MIN_NUM, MAX_NUM)
    question = random_num
    correct_answer = is_even(question)
    if is_even(question) is False:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return question, correct_answer


def is_even(question):
    """Checks if the number is even."""
    if question % 2 == 0:
        return True
    else:
        return False
