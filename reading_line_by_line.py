file_path = "pcc_3e-main/chapter_10/reading_from_a_file/pi_digits.txt"
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())