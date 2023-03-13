import csv

# Sample data
data = [
    ('Name', 'Age', 'Gender'),
    ('Alice', '25', 'Female'),
    ('Bob', '30', 'Male'),
    ('Charlie', '', 'Male'),
]

# Open a file for writing with 'w' mode and newline='' to avoid line ending issues
with open('output.tsv', 'w', newline='') as f:
    # Create a CSV writer object with tab as delimiter
    writer = csv.writer(f, delimiter='\t')
    
    # Write the data rows
    for row in data:
        writer.writerow(row)

f.close()


for row in data:
    print(row)
