import random


game_rules = "What number is missing in the progression?"


def question_func():
    start = random.randint(2, 10)
    step = random.randint(1, 100)
    random_index = random.randint(2, 5)
    new_list = [(start + i * step) for i in range(random.randint(6, 10))]
    new_list.pop(random_index)
    new_list.insert(random_index, "..")
    return new_list


def correct_answer(question):
    step = question[1] - question[0]
    for index, elem in enumerate(question):
        if elem == '..':
            d = index - 1
            secret_num = question[d] + step
            break
    correct_answer = secret_num
    return str(correct_answer)
