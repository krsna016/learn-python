def count_specific_word(file_path):
    """
    This function could be used to count the specific word
    in the file.
    """
    try:
        with open(file_path) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print("...File does not exist...")
    else:
        word = input("Enter the word to count the total occurance : ").lower()
        counter = content.lower().count(word)
        print(f"The total '{word}'s : {counter}")

        
file_path = "Python_crash_course_files/txt_files/book.txt"
count_specific_word(file_path)