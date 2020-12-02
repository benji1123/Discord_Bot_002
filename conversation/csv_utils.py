import csv


def get_dialog_dict(data_path: str) -> dict:
    """Return a map from conversational prompts to responses"""
    dialog_dict = {}
    with open(data_path) as csv_file:
        lines = csv.reader(csv_file, delimiter=',')
        for line in lines:
            prompt = line[0]
            response_pool = [resp for resp in line[1:] if resp != ""]
            dialog_dict[prompt] = response_pool
    return dialog_dict
