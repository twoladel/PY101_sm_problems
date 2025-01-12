def clean_up(my_str):
    my_list = []
    for char in my_str:
        if char.isalpha():
            my_list.append(char)
        else:
            my_list.append(' ')

    cleaned = []
    if my_list[0].isspace():
        cleaned.append(' ')

    for i in range(len(my_list)):
        if not my_list[i - 1].isspace() and my_list[i].isspace():
            cleaned.append(my_list[i])
        if my_list[i].isalpha():
            cleaned.append(my_list[i])
    cleaned = ''.join(cleaned)
    print(cleaned)
    return cleaned


print(clean_up("---what's my +*& line?") == " what s my line ")
# True