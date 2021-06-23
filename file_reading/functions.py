
def display_file(file_input):

    line_count = 0

    for file_line in file_input:
        
        
        if file_line == '\0' or file_line == '\n':
            print(f"{line_count}: [ blank line ]")
        else:
            file_line = file_line.replace('\n', '')
            print(f"{line_count}: {file_line} [{count_non_space(file_line)} letters, {count_spaces(file_line)} spaces, {count_words(file_line)} words]")

        line_count += 1


def verify_char(input_char):
    char_value = ord(input_char)
    upper_case = char_value >= 65 and char_value <= 90
    lower_case = char_value >= 97 and char_value <= 122
    is_char = False

    if(upper_case):
        is_char = True
    elif(lower_case):
        is_char = True
    
    return is_char


def count_non_space(line_of_text):

    char_count = 0

    for i in line_of_text:
        if verify_char(i):
            char_count += 1
    
    return char_count
        

def count_spaces(line_of_text):
    
    space_count = 0

    for i in line_of_text:
        if i == ' ':
            space_count += 1
    
    return space_count


def count_words(line_of_text):
    
    word_count = 0
    on_word = False
    on_space = False

    for i in line_of_text:

        if(verify_char(i) and on_word == False):
            word_count += 1
            on_word = True
            on_space = False
        
        if(i == ' ' and on_space == False):
            on_word = False
            on_space = True

    return word_count


