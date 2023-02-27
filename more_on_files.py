import sys
import os
from pathlib import Path
path = Path().home() # Path to home dir
path_1 = Path().cwd() # Path to current working dir
path_2 = Path().cwd() / "8-Python" # Actual path
path_3 = Path("8-Python") # Relative path

print("Home path :".ljust(30),path)
print("Current working directory :".ljust(30),path_1)
print("Actual path :".ljust(30),path_2)
print("Relative path :".ljust(30),path_3)
print("Platform :".ljust(30),sys.platform)

os.chdir("1-Numpy-module") # Change the dir
path_a = Path().cwd() # Path to current working dir
print(f"Directory changed to :".ljust(30),path_a)

os.chdir("..")
path_a = Path().cwd() # Path to current working dir
print(f"Directory changed to :".ljust(30),path_a)

# Path(Path().cwd() / "Created_one").mkdir()
print((Path.cwd() / "/-Python").is_absolute())
print((Path.cwd()).is_absolute())

os.chdir('..')
print(Path.cwd())
list_dir = os.scandir("WannaDoPython")
for i in list_dir:
    print(i)
os.chdir("WannaDoPython")
print(Path.cwd())
# os.mkdir("Created_one_other")
os.path.abspath("8-Python")

print(os.path.abspath(".."))
print(os.path.abspath("."))
print(os.path.relpath("/1-Numpy-module"))
