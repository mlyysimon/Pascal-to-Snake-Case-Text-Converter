def convert_to_snake_case(pascal_or_camel_cased_string):
    # get rid of any accidental spaces in string input
    text_convert = str.maketrans({' ': ''})
    clean_string = pascal_or_camel_cased_string.translate(text_convert)

    # if the string is already in snake case, return it as is
    # uppercase indicates the start of a new word, so in that case, change to lowercase and add an underscore before it
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in clean_string
    ]

    # join letters into string and remove any leading or trailing underscores
    return ''.join(snake_cased_char_list).strip('_')

def main():
    
    while True:
        print('\nPascal to Snake Case Text Converter')
        choice = input("1. Convert a string\n2. Exit\n\nEnter your choice: ")
        
        if choice == '1':
            string = input("\nEnter a Pascal cased string: ")
            print(f'\nSnake cased string: {convert_to_snake_case(string)}')
        elif choice == '2':
            print("\nExiting the program.")
            break
        
if __name__ == '__main__':
    main()