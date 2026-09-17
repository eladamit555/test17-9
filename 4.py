other_string = set()
its_right = False
while True:
    word = input('enter a string: ')
    if word == 'quit':
        break
    if word[::-1] in other_string:
        its_right = True
        break
    other_string.add(word)
if its_right:
    print('reversed match found')
else:
    print('no reversed match found')



