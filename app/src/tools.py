import os

INPUT = './input'
OUTPUT = './output'

def clear_folders():
   try:
     files = os.listdir(INPUT)
     for file in files:
       file_path = os.path.join(INPUT, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
     print("All files in INPUT deleted successfully.")

     files = os.listdir(OUTPUT)
     for file in files:
       file_path = os.path.join(OUTPUT, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
     print("All files in OUTPUT deleted successfully.")
   except OSError:
     print("Error occurred while deleting files.")