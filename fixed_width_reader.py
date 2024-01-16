import pandas as pd

def fixed_width_to_csv(input_file, output_file, widths):
    # Define column names based on the fixed widths
    column_names = [f'col{i+1}' for i in range(len(widths))]

    # Read the fixed-width file using pandas read_fwf
    df = pd.read_fwf(input_file, widths=widths, names=column_names)

    # Write the DataFrame to a CSV file
    df.to_csv(output_file, index=False)

# Example usage
input_file = '/Users/rajeev/Rajeev-Local/Study/Python/Python_Utils/Test_Data/generated_file.txt'
output_file = '/Users/rajeev/Rajeev-Local/Study/Python/Python_Utils/Test_Data/output_csv_file.csv'
widths = [10, 15, 8, 12, 10, 20, 15, 8, 10, 10]  # Example widths for each column

fixed_width_to_csv(input_file, output_file, widths)
