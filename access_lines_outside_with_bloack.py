file_path = "pcc_3e-main/chapter_10/reading_from_a_file/pi_digits.txt"
with open(file_path) as file_object:
    list_1 = file_object.readlines()
for line in list_1:
    print(line.rstrip())