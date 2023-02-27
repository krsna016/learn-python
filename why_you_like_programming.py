file_name = "Python_crash_course_files/txt_files/reason.txt"
while True:
    name = input("Enter the name : \n")
    reason = input("Why you like programming ? : \n")
    if(name == "" or reason == ""):
        print("...Data saved...")
        break
    else:
        with open(file_name,"w") as file_object:
            file_object.write(f"Name : {name}\nReason : {reason}\n")
