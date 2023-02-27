with open("pcc_3e-main/chapter_10/reading_from_a_file/pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())