file_path = "C:/Users/KNAGASRE/OneDrive - Capgemini/Desktop/slog/Python/python_files/welcome.txt"

file_object = open(file_path,"a")
file_content = file_object.writelines(" Hello world 9")
print(file_content)
print(file_object.closed)
file_object.close()


print(file_object.name)
print(file_object.mode)
print(file_object.closed)
