from faker import Faker

fake = Faker()

def generate_fake_data(rows, column_widths):
    data = []
    for _ in range(rows):
        row = [fake.text(width) for width in column_widths]
        data.append(row)
    return data

def write_fixed_width_file(file_path, data, column_widths):
    with open(file_path, 'w') as file:
        for row in data:
            formatted_row = ''.join(f'{value:{width}}' for value, width in zip(row, column_widths))
            file.write(formatted_row + '\n')

# Example usage:
num_rows = 100
num_columns = 10
column_widths = [10, 15, 8, 12, 10, 20, 15, 8, 10, 10]

fake_data = generate_fake_data(num_rows, column_widths)

file_path = '/Users/rajeev/Rajeev-Local/Study/Python/Python_Utils/Test_Data/generated_file.txt'
write_fixed_width_file(file_path, fake_data, column_widths)

print(f"Fixed-width file generated at {file_path}")
