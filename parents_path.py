import pathlib
path_1 = pathlib.Path().cwd()
print(path_1)
print(path_1.parents[0])
print(path_1.parents[1])
print(path_1.parents[2])
print(path_1.parents[3])