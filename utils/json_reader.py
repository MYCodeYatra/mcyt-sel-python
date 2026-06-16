import json
def get_data_from_json(file_path):
    with open(file_path, mode='r') as file:
        json_data = json.load(file)
    data = []
    for item in json_data:
        data.append((item["username"], item["password"], item["expected"]))
    return data