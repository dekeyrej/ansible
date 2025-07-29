import yaml
import json

def parse_markdown_table(markdown_string):
    lines = markdown_string.strip().split('\n')
    
    # Extract headers
    headers = [h.strip() for h in lines[0].split('|') if h.strip()]
    
    data = []
    for line in lines[2:]:  # Skip header and separator lines
        row_values = [v.strip() for v in line.split('|') if v.strip()]
        if len(row_values) == len(headers):
            data.append(dict(zip(headers, row_values)))
    return data

markdown_table = """
| Product | Brand | Price |
|---------|-------|-------|
| Smartphone | Apple | 999.99 |
| Laptop | Dell | 1299.99 |
"""

parsed_data = parse_markdown_table(markdown_table)
# print(yaml.dump(parsed_data, default_flow_style=False))
print(json.dumps(parsed_data, indent=2))

from py_markdown_table.markdown_table import markdown_table
markdown_output = markdown_table(parsed_data).get_markdown()
print(markdown_output)