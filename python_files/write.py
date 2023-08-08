file_path = "C:/Users/KNAGASRE/OneDrive - Capgemini/Desktop/slog/Python/python_files/welcome.txt"

file_object = open(file_path,"a")
file_content = file_object.write("hello world")
print(file_content)
file_object.close()