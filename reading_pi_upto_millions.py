file_path = "pcc_3e-main/chapter_10/reading_from_a_file/pi_million_digits.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()
millions = ""
for line in lines: 
    millions += line.strip()
print(millions[:52] + "...")
print(len(millions))
