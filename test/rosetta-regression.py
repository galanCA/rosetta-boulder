import sys
sys.path.insert(0,'../src')
from rosetta import Rosetta

latticeFF = Rosetta()
for i,r in latticeFF.data.iterrows():
    print(i, r)