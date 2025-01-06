def print_border(width):
    print('+' + ('-' * width) + '+')

def print_padding(width):
    print('|' + (' ' * width) + '|')

def wrapped_in_box(string, max=75):
    width = len(string) + 2

    if max < len(string) + 4:

        width = max - 2
        print_border(width)
        print_padding(width)

        lines = ((len(string) + 4) // max) + 1
        step = max - 4
        end = step
        for i in range(0, step * lines, step):
            if len(string) < end:
                buffer = end - len(string)
                print(f'| {string[i:end]}' + ' ' * buffer + ' |')
            else:
                print(f'| {string[i:end]} |')
            end += step

        print_padding(width)
        print_border(width)

    else:
        for i in range(5):
            if i == 0 or i == 4:
                print('+' + ('-' * width) + '+')
            elif i == 1 or i == 3:
                print('|' + (' ' * width) + '|')
            else:
                print(f'| {string} |')

wrapped_in_box('To boldly go where no one has gone before.', 20)
wrapped_in_box('To boldly go where no one has gone before.')
wrapped_in_box('')
wrapped_in_box(
    'Twas the night before christmas and all through the house, not a creature '
    'was stirring, not even a mouse. When all of a sudden, there arose such a '
    'clatter, that ma and pa sprung from their beds to see what was the matter!'
, 70)
