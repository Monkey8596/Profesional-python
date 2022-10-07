

def edges(func):
    
    def wrapper(text):
        print(' '+ '_' * (1 + len(text)))
        print('/'+ '_' * (len(text)) + '/|' )
        print('|'+ ' ' * (len(text)) + '||' )
        func('|' + text + '||' )
        print('|'+ '_' * (len(text)) + '|/' )

    return wrapper

@edges
def _print_(text):
    print(text)

def run():
    text = input ('Write a text: ')
    _print_(text)

if __name__ == '__main__':
    run()
