import random


GAME_RULES = "Find the greatest common divisor of given numbers."
MIN_NUM = 1
MAX_NUM = 100


def generate_round():
    """Generates a random question and returns it and the correct answer."""
    random_num_1 = random.randint(MIN_NUM, MAX_NUM)
    random_num_2 = random.randint(MIN_NUM, MAX_NUM)
    question = str(random_num_1), str(random_num_2)
    correct_answer = get_gcd(random_num_1, random_num_2)
    output_question = " ".join(question)
    return output_question, str(correct_answer)


def get_gcd(a, b):
    """Counts the greatest common divisor."""
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    correct_answer = (a + b)
    return correct_answer
