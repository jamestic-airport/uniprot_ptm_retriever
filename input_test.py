import pprint

with open('proteins.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()

    # Strip any whitespace characters (including newline characters) from each line
    lines = [line.strip() for line in lines]

file.close

for protein in lines:
    print(protein)