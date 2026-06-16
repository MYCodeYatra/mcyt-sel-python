import csv
def get_data_from_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader) # Skip the header row
        for row in reader:
            data.append(tuple(row)) # Convert list to tuple
    return data