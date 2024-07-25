file_path = '/home/max/Documents/projetos/python_crash_course/chapt_10_files_and_exceptions/files/greetings.txt'

try:
    with open(file_path, 'a') as file_object:
        file_object.write("I'm studying algorithms and Python programing.\n")
        file_object.write("I'm becoming a software engineer.\n")
        file_object.write("I'm changing my life for better.\n")
    
except FileNotFoundError:
    print("File not found or directory does not exist.\n")

else:
    try:
        with open(file_path, 'r') as file_object:
            content = file_object.readlines()
            for line in content:
                print(line.strip())

    except FileNotFoundError:
        print("File not found when trying to read")
