import os

folder_path = os.getcwd()
output_file_path = 'trees.txt'

treefile_list = [file for file in os.listdir(folder_path) if file.endswith('.treefile')]

with open(output_file_path, 'w') as output_file:
    for treefile in treefile_list:
        treefile_path = os.path.join(folder_path, treefile)
        with open(treefile_path, 'r') as current_file:
            output_file.write(current_file.read())