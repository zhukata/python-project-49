import random


GAME_RULES = "Find the greatest common divisor of given numbers."
MIN_NUM = 1
MAX_NUM = 100


def get_question():
    random_num = random.randint(MIN_NUM, MAX_NUM)
    random_num_2 = random.randint(MIN_NUM, MAX_NUM)
    question = str(random_num), str(random_num_2)
    a = random_num
    b = random_num_2
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    correct_answer = (a + b)
    output_question = " ".join(question)
    return output_question, str(correct_answer)
