import os

MAX_FILE_SIZE = 100 * 1024  # 100 KiB
input_file = "overshoot.txt"
output_directory = "output"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

with open(input_file, "r") as f:
    file_number = 1
    current_file_size = 0
    current_output_file = open(f"{output_directory}/output{file_number}.txt", "w")

    for line in f:
        current_file_size += len(line.encode('utf-8'))
        if current_file_size > MAX_FILE_SIZE and line.strip() == "":
            current_output_file.close()
            file_number += 1
            current_file_size = 0
            current_output_file = open(f"{output_directory}/output{file_number}.txt", "w")
        current_output_file.write(line)

    current_output_file.close()
