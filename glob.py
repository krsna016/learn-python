import os
from pathlib import Path
path = Path("1-Numpy-module")
s = list(path.glob("*"))
for i in s:
    print(i)
print("\n\n")
p = list(path.glob("*.txt"))
for i in p:
    print(i)
print("\n\n")

