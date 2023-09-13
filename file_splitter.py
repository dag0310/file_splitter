import sys
import os
import datetime

if len(sys.argv) < 3:
    print('Example usage: python3 file_splitter.py test.txt 100')
    quit()

filepath = sys.argv[1]
max_kb_per_file = int(sys.argv[2]) * 1024

filename_tokens = os.path.basename(filepath).split('.')
filename_without_extension = filename_tokens[-2]
filename_extension = filename_tokens[-1]
current_date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_folderpath = os.path.join('output', filename_without_extension + '_' + current_date_time)

with open(sys.argv[1], "r") as f:
    if not os.path.exists(output_folderpath):
        os.makedirs(output_folderpath)
    file_number = 1
    current_file_size = 0
    current_output_file = open(f"{output_folderpath}/{filename_without_extension}_{file_number}.{filename_extension}", "w")

    for line in f:
        current_file_size += len(line.encode('utf-8'))
        if current_file_size > max_kb_per_file and line.strip() == "":
            current_output_file.close()
            file_number += 1
            current_file_size = 0
            current_output_file = open(f"{output_folderpath}/{filename_without_extension}_{file_number}.{filename_extension}", "w")
        current_output_file.write(line)

    current_output_file.close()

print('Split files written successfully to "' + output_folderpath + '"')
