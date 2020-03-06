import os

script_dir = os.path.dirname(__file__) # get current address
rel_path = "users/example.txt"
abs_file_path = os.path.join(script_dir, rel_path) # join addresses

with open(str(abs_file_path),"w") as f:
    f.close()
