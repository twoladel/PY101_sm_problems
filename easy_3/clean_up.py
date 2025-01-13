def clean_up(my_str):
    my_list = []
    for char in my_str:
        if char.isalpha():
            my_list.append(char)
        else:
            my_list.append(' ')
    
    return remove_spaces(my_list)

def remove_spaces(lst):
    cleaned = []
    if lst[0].isspace():
        cleaned.append(' ')

    for i in range(len(lst)):
        if not lst[i - 1].isspace() and lst[i].isspace():
            cleaned.append(lst[i])
        if lst[i].isalpha():
            cleaned.append(lst[i])
            
    cleaned = ''.join(cleaned)

    return cleaned


print(clean_up("---what's my +*& line?") == " what s my line ")
# True