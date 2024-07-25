file_path = '/home/max/Documents/projetos/python_crash_course/chapt_10_files_and_exceptions/files/programming.txt'

try:
    with open(file_path, 'w') as file_object:
        file_object.write("I love programming.\n")
        file_object.write("I love creating business apps.\n")
        file_object.write("I help my costumers improve theirs business.\n")

except FileNotFoundError:
    print("File not found or direct does not exist")

else:
   try:
        with open(file_path, 'r') as file_object:
            content = file_object.readlines()
            for line in content:
                print(line.strip())

   except FileNotFoundError:
        print("File not found when trying to read")