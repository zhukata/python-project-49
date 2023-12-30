import random


game_rules = "What is the result of the expression?"

operator = ['+', '-', '*']


def question_func():
    random_num = random.randint(1, 100)
    random_num_2 = random.randint(1, 100)
    random_operator = random.choice(operator)
    question = f"{random_num} {random_operator} {random_num_2}"
    return question


def correct_answer(question):
    correct_answer = eval(question)
    return str(correct_answer)
