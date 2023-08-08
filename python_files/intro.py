# creating new text file called intro.txt

file_path = "C:/Users/KNAGASRE/OneDrive - Capgemini/Desktop/slog/Python/python_files/intro.txt"

file_object = open(file_path,"x")
file_content = file_object.writelines("Hello this is HK")
print(file_content)
file_object.close()