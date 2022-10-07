

def decorator(func):
    
    def second():
        print('Adding to the first function')
        func()

    return second

@decorator
def hi():
    print('Hi!')

hi()
