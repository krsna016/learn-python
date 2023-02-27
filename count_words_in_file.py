def count_words(file_path):
    """This function is used to count the number of words in the file"""
    try:
        with open(file_path) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print(f"...Sorry the file : {file_path} does not exist...")
    else:
        words = content.split()
        print(f"The total number of words in the file are : {len(words)}")


file_path = "Python_crash_course_files/txt_files/alice_in_wonderland.txt"
count_words(file_path)