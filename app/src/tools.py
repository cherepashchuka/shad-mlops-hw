import os

INPUT = './input'
OUTPUT = './output'

def clear_folders():
   print('### Delete files in INPUT ###')
   try:
     files = os.listdir(INPUT)
     for file in files:
       file_path = os.path.join(INPUT, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
     print('### Delete files in INPUT -- Successful###')

     print('### Delete files in OUTPUT ###')
     files = os.listdir(OUTPUT)
     for file in files:
       file_path = os.path.join(OUTPUT, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
     print('### Delete files in OUTPUT -- Successful###')
   except OSError:
     print("Error occurred while deleting files.")