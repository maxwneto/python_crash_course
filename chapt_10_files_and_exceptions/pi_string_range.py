file_path = '/home/max/Documents/projetos/python_crash_course/chapt_10_files_and_exceptions/files/pi.txt'

try:
    with open(file_path) as  file_object:
        lines = file_object.readlines()

except FileNotFoundError:
        print("File not found or does not exitst")

else:
     pi_string = ''
     for line in lines:
          pi_string += line.strip()

     print(pi_string[:52] + "...")
     print(len(pi_string))