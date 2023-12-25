

def check_even_num(x):
    if x % 2 == 0:
        return True
    return False


def check_answer(text, random_num):
    if text == 'yes':
        if check_even_num(random_num):
            return True
    elif text == 'no':
        if check_even_num(random_num):
            return False
        return True
    return False
