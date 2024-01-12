import random


GAME_RULES = """Answer "yes" if given number is prime. Otherwise answer "no"."""
MIN_NUM = 1
MAX_NUM = 3000


def generate_round():
    """Generates a random question and returns it and the correct answer"""
    question = random.randint(MIN_NUM, MAX_NUM)
    if is_prime(question) is False:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return question, correct_answer


def is_prime(question):
    """Checks if the number is prime."""
    counter = 0
    for i in range(2, question // 2 + 1):
        if (question % i == 0):
            counter += 1
    if (counter <= 0):
        return True
    else:
        return False
