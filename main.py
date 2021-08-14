def str_replace_interface():
    word = input("Enter a word: ")
    if word != 'quit':
        substring = input("Please enter the substring you wish to find: ")
        new_entry = input("Please enter a string to replace the given substring: ")
        new_word = word.replace(substring, new_entry)
        print("Your new string is: " + new_word)
        str_replace_interface()

str_replace_interface()