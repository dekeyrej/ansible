import yaml
import json

with open('roles/Monolithic_role_list.md', 'r') as file:
    markdown_table = file.read()


def parse_markdown_table(markdown_string):
    lines = markdown_string.strip().split('\n')
    
    list_fields = ['Called In', 'Depends On']
    # Extract headers
    headers = [h.strip() for h in lines[0].split('|') if h.strip()]
    
    data = []
    for line in lines[2:]:  # Skip header and separator lines
        row_values = [v.strip() for v in line.split('|') if v.strip()]
        for i, header in enumerate(headers):
            if header in list_fields and i < len(row_values):
                row_values[i] = [item.strip() for item in row_values[i].split(',')]

        if len(row_values) == len(headers):
            data.append(dict(zip(headers, row_values)))
    return data

def list_of_dicts_to_dict_of_dicts(list_of_dicts, key):
    """
    Converts a list of dictionaries into a dictionary of dictionaries using the specified key.
    
    :param list_of_dicts: List of dictionaries to convert.
    :param key: The key to use as the new dictionary's keys.
    :return: A dictionary where each key is the value from the specified key in the original dictionaries.
    """
    dict_of_dicts = {d[key]: d for d in list_of_dicts if key in d}

    return {k.replace('`', ''): v for k, v in dict_of_dicts.items()}


parsed_data = parse_markdown_table(markdown_table)
restructured_data = list_of_dicts_to_dict_of_dicts(parsed_data, 'Role Name')
# print(yaml.dump(parsed_data, default_flow_style=False))
print(json.dumps(restructured_data, indent=2))

# from py_markdown_table.markdown_table import markdown_table
# markdown_output = markdown_table(parsed_data).get_markdown()
# print(markdown_output)