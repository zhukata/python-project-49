import prompt


def lose_game(answer, correct_answer, name):
    print(f""""{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".
Let's try again, {name}!""")


def congratulations(name):
    print(f"Congratulations, {name}!")


def check_answer(answer, correct_answer):
    if answer != correct_answer:
        return False
    return True


def engine_func(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name?')
    print(f"Hello, {name}")
    print(game.game_rules)
    for i in range(0, 3):
        question = game.question_func()
        print(f"Question: {question}")
        answer = prompt.string("Your answer:")
        correct_answer = game.correct_answer(question)
        if check_answer(answer, correct_answer) == False:
            return lose_game(answer, correct_answer, name)
        print("Correct!")
    return congratulations(name)
