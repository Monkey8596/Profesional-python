

def Upper_letters(func):

    def second(text):
        return func(text).upper()

    return second

@Upper_letters
def message (name):
    return f'{name}, you receive a message'

print(message('Cesar'))