import random


GAME_RULES = "What is the result of the expression?"
OPERATOR = ['+', '-', '*']
MIN_NUM = 1
MAX_NUM = 100


def get_question():
    """Generates a random question and returns it and the correct answer."""
    random_num = random.randint(MIN_NUM, MAX_NUM)
    random_num_2 = random.randint(MIN_NUM, MAX_NUM)
    operator = random.choice(OPERATOR)
    question = f"{random_num} {operator} {random_num_2}"
    correct_answer = get_correct_answer(operator, random_num, random_num_2)
    return question, str(correct_answer)


def get_correct_answer(operator, random_num, random_num_2):
    """Counts the correct answer of the expression"""
    if operator == '+':
        correct_answer = random_num + random_num_2
    elif operator == '-':
        correct_answer = random_num - random_num_2
    else:
        correct_answer = random_num * random_num_2
    return correct_answer
