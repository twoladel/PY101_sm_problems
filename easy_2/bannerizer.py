# define a function called print in box
# take a string argument
# print string in center of box
# box structure: + for corners, - for top/bottom border, | for side borders
# box min size is two chars across, three down. 
# need length of string 
# width of box should be string length plus 4 
# We have corners, amount of dashes and spaces should equal string length + 2
# use loop
# print one line at a time, 5 lines total

def print_in_box(string):
    width = len(string) + 2
    for i in range(5):
        if i == 0 or i == 4:
            print('+' + ('-' * width) + '+')
        elif i == 1 or i == 3:
            print('|' + (' ' * width) + '|')
        else:
            print(f'| {string} |')

print_in_box('To boldly go where no one has gone before.')
print_in_box('')