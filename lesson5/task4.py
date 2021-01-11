trans = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open('task4_input.txt', 'r') as input_file, open('task4_output.txt', 'w') as output_file:
    for row in input_file.readlines():
        row_parts = [row_part.strip() for row_part in row.split('-')]
        output_file.write(row.replace(row_parts[0], trans[row_parts[0]]))
