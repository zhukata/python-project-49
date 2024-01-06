import prompt


def check_answer(answer, correct_answer):
    if answer != correct_answer:
        return False
    return True


def generate_round(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name?')
    print(f"Hello, {name}")
    print(game.GAME_RULES)
    for i in range(0, 3):
        question, correct_answer = game.get_question()
        print(f"Question: {question}")
        answer = prompt.string("Your answer:")
        if check_answer(answer, correct_answer) is False:
            return print(f""""{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".
Let's try again, {name}!""")
        print("Correct!")
    return print(f"Congratulations, {name}!")
