import os


dir_path = os.path.abspath('.')
# abs_path = os.path.abspath('..')
file_name = 'tuples.py'
# file_path = dir_path + '\\' + file_name
file_path = os.path.join(dir_path, file_name)
# print(file_path)

path_is_dir = os.path.isdir('.')
path_is_file = os.path.isfile(file_path)

# print(help(os))
# print(path_is_file)
# print(path_is_dir)


# os.system('mkdir example')
# os.system('rmdir example')

# folder = os.listdir('.')

# os.system('mkdir example')

for filename in os.listdir('.'):
    if os.path.isfile(filename):
        abs_path = os.path.join(os.path.abspath('.'), filename)
        print(abs_path)
    elif os.path.isdir(filename):
        print(filename, '->', 'directory')
