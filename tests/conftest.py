import sys
import os 

project_root = os.path.join(os.path.dirname(__file__), '..')
print("** project_root:", project_root)
sys.path.insert(0,project_root)
print(sys.path)