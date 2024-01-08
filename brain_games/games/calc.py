import random


GAME_RULES = "What is the result of the expression?"
OPERATOR = ['+', '-', '*']
MIN_NUM = 1
MAX_NUM = 100


def get_question():
    """Generates a random question and returns it and the correct answer."""
    random_num = random.randint(MIN_NUM, MAX_NUM)
    random_num_2 = random.randint(MIN_NUM, MAX_NUM)
    random_operator = random.choice(OPERATOR)
    question = f"{random_num} {random_operator} {random_num_2}"
    if random_operator == '+':
        correct_answer = random_num + random_num_2
    elif random_operator == '-':
        correct_answer = random_num - random_num_2
    else:
        correct_answer = random_num * random_num_2
    return question, str(correct_answer)
