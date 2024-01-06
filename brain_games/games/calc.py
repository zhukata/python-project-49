import random


GAME_RULES = "What is the result of the expression?"
OPERATOR = ['+', '-', '*']
MIN_NUM = 1
MAX_NUM = 100


def get_question():
    random_num = random.randint(MIN_NUM, MAX_NUM)
    random_num_2 = random.randint(MIN_NUM, MAX_NUM)
    random_operator = random.choice(OPERATOR)
    question = f"{random_num} {random_operator} {random_num_2}"
    correct_answer = eval(question)
    return question, str(correct_answer)
