file_path = "pcc_3e-main/chapter_10/reading_from_a_file/pi_digits.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()
in_one_line = ""
for line in lines:
    in_one_line += line.strip()
print(in_one_line)
print(len(in_one_line))
