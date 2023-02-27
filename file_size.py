import os,pathlib
# path_1 = pathlib.Path().cwd()
# for files in os.scandir(path_1):
#     print(files)

path_1 = pathlib.Path().cwd()
print(path_1)
print(os.path.getsize(path_1 / "PROJECT_10_ALIEN_INVASION-pygame"))
total_size = 0
for files in os.listdir(path_1):
    total_size += os.path.getsize(os.path.join(path_1,files))
print(total_size)

