import random


GAME_RULES = "What number is missing in the progression?"
MIN_NUM = 1
MAX_NUM = 100
MAX_INDEX_NUM = 5
MAX_START_NUM = 10


def get_question():
    start = random.randint(MIN_NUM, MAX_START_NUM)
    step = random.randint(MIN_NUM, MAX_NUM)
    random_index = random.randint(MIN_NUM, MAX_INDEX_NUM)
    new_list = [(start + i * step) for i in range(random.randint(MAX_INDEX_NUM, MAX_START_NUM))]
    correct_answer = new_list.pop(random_index)
    new_list.insert(random_index, "..")
    question = []
    for i in new_list:
        question.append(str(i))
    output_question = " ".join(question)
    return output_question, str(correct_answer)
