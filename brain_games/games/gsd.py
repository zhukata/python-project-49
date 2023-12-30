import random


game_rules = "Find the greatest common divisor of given numbers."


def question_func():
    random_num = random.randint(1, 100)
    random_num_2 = random.randint(1, 100)
    question = random_num, random_num_2
    return question


def correct_answer(question):
    a = question[0]
    b = question[1]
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    correct_answer = (a + b)
    return str(correct_answer)
