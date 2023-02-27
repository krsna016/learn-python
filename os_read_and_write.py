import pathlib,os 
os.chdir("..")
path_1 = pathlib.Path("Desktop/WannaDoPython/created.txt")
path_1.write_text("Hello")
print(path_1.read_text())