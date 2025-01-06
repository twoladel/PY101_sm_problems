def crunch(string):
    collapsed = []
    for index in range(len(string)):
        if index == (len(string) -1) or string[index] != string[index + 1]:
            collapsed.append(string[index])

    return ''.join(collapsed)

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')