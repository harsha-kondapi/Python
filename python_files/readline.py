file_path = "C:/Users/KNAGASRE/OneDrive - Capgemini/Desktop/slog/Python/python_files/welcome.txt"

file_object = open(file_path,"r")
file_content = file_object.readline()
print(file_content)
file_object.close()