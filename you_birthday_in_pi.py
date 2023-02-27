# Method - 1:

# file_path = "pcc_3e-main/chapter_10/reading_from_a_file/pi_million_digits.txt"
# with open(file_path) as file_object:
#     lines = file_object.readlines()
# pi_millions = ""
# for line in lines:
#     pi_millions += line.strip()
# b_d = input("Enter your birth date in format ddmmyy : ")
# if b_d in pi_millions:
#     print("...Your birthdate comes in first million numbers of pi...")
# else:
#     print("...Your birthdate not comes in pi...")
        
    

# Method - 2:

file_path = "pcc_3e-main/chapter_10/reading_from_a_file/pi_million_digits.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()
pi_millions = ""
for line in lines:
    pi_millions += line.strip()
b_d = input("Enter your birth date in format ddmmyy : ")

flag = 0

for i in range(len(pi_millions)):
    if(b_d in pi_millions[i:i+6]):
        flag = 1
if(flag == 1):
    print("...Your birthdate comes in first million numbers of pi...")
else:
    print("...Your birthdate not comes in pi...")

        
