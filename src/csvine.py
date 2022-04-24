def parse(file_path: str, delimiter: str = None) -> str:
    if delimiter == None:
        delimiter = ','
    with open(file_path, 'r') as file:
        return [row.split(delimiter) for row in ''.join(file.read()).split('\n')]

#def __delimiters_indices__(header: str, delimiter: str) -> list:
#    return [index for index in range(0, len(header)) if header.startswith(delimiter, index)]

def filter_for_coordinates(csv_data: list, header_key: str, value: str, delimiter: str = None) -> tuple:
    if delimiter == None:
        delimiter = ','
    
    group = csv_data[0].index(header_key)
    for i, row in enumerate(csv_data):
        if row[group] == value:
            return (group, i)
    return -1

def replace(csv_data: list, coordinates: tuple, value: str) -> str:
    csv_data[coordinates[1]][coordinates[0]] = value
    return csv_data

def insert(csv_data: list, coordinates: tuple, value: str, delimiter: str = None) -> str:
    if delimiter == None:
        delimiter = ','
    nrows = coordinates[1] - len(csv_data)
    if nrows >= 0:
        csv_data += [[''] * len(csv_data[0]) for _ in range(nrows + 1)]
    csv_data[coordinates[1]][coordinates[0]] = value
    return csv_data

def save(csv_data: list, file_path: str, delimiter: str = None) -> None:
    if delimiter == None:
        delimiter = ','
    with open(file_path, 'w') as file:
        file.write('\n'.join([str(delimiter).join(row) for row in csv_data]))