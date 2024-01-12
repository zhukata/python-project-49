import random


GAME_RULES = "What number is missing in the progression?"

MIN_NUM = 1
MAX_NUM = 100

MAX_INDEX_NUM = 5
MAX_START_NUM = 10

MIN_RANGE_NUM = 6


def generate_round():
    """Generates a random question and returns it and the correct answer."""
    random_index = random.randint(MIN_NUM, MAX_INDEX_NUM)
    progression = generate_progression()
    correct_answer = progression.pop(random_index)
    progression.insert(random_index, "..")
    question = []
    for i in progression:
        question.append(str(i))
    output_question = " ".join(question)
    return output_question, str(correct_answer)


def generate_progression():
    """Generates a random progression"""
    start = random.randint(MIN_NUM, MAX_START_NUM)
    step = random.randint(MIN_NUM, MAX_NUM)
    progression = [
        (start + i * step)
        for i in range(random.randint(MIN_RANGE_NUM, MAX_START_NUM))
    ]
    return progression
