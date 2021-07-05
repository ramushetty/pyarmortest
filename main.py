import sys
import os

path = os.path.abspath(".")

sys.path.append(path + "/dist")


from algorithms.myalgo1 import hello1 
from algorithms.myalgo2 import hello2

print(hello1())
print(hello2())
