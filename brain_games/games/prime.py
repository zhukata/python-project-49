import random


GAME_RULES = """Answer "yes" if given number is prime. Otherwise answer "no"."""
MIN_NUM = 1
MAX_NUM = 3000


def get_question():
    """Generates a random question and returns it and the correct answer"""
    question = random.randint(MIN_NUM, MAX_NUM)
    correct_answer = isPrime(question)
    return question, correct_answer


def isPrime(question):
    """Checks if the number is prime."""
    counter = 0
    for i in range(2, question // 2 + 1):
        if (question % i == 0):
            counter += 1
    if (counter <= 0):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
