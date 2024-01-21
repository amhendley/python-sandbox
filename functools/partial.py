from functools import partial
print_no_newline = partial(print, end=', ')

print('Normal print() behavior:')
for _ in range(3):
    print('test')


print('My new frozen print() one:')
for _ in range(3):
    print_no_newline('test')

