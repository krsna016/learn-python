# Importing time and sys module:
import time,sys
# Taking the height of the zigzag from the user:
height = int(input("Enter the height of the zigzag : "))
spaces = 0
indent_increase = True
# Using try-except statement:
try:
    while True:
        print(spaces * " " + "********************")
        time.sleep(0.1)
        # Indentation increase:
        if indent_increase:
            spaces += 1
            if(spaces == height):
                indent_increase = False
        # Indentation decrease:
        else:
            spaces -= 1
            if(spaces == 0):
                indent_increase = True
except KeyboardInterrupt:
    sys.exit()
        