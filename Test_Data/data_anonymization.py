import pandas as pd
import faker

def anonymize_csv(input_file, output_file, columns_to_anonymize):
    # Load CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Initialize Faker generator for creating fake data
    fake = faker.Faker()

    # Anonymize specified columns
    for column in columns_to_anonymize:
        if column in df.columns:
            # Replace values with appropriate fake data based on column type
            if df[column].dtype == 'object':  # String data
                df[column] = df[column].apply(lambda x: fake.name() if pd.notnull(x) else x)
            elif df[column].dtype == 'float64':  # Numeric data
                df[column] = df[column].apply(lambda x: fake.random_number() if pd.notnull(x) else x)

    # Save the anonymized DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

# Example usage
input_file = 'input_data.csv'
output_file = 'anonymized_data.csv'
columns_to_anonymize = ['Name', 'Email', 'Phone']

anonymize_csv(input_file, output_file, columns_to_anonymize)
