some_letters = ['a','b','c','d','e','f']
it = iter(some_letters)
while True:
    try:
        letter = next(it)
    except StopIteration:
        print('end of iteration')
        break
    print(letter)