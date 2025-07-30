# python role_meteadata.py > roles/generated_roles_list.md

import os
import yaml
from py_markdown_table.markdown_table import markdown_table

def get_ansible_roles(ansible_project_path):
    roles_found = []
    roles_path = os.path.join(ansible_project_path, 'roles')
    if not os.path.exists(roles_path):
        return roles_found

    for role_name in os.listdir(roles_path):
        role_dir = os.path.join(roles_path, role_name)
        if os.path.isdir(role_dir):
            meta_file = os.path.join(role_dir, 'meta', 'data.yaml')
            if os.path.exists(meta_file):
                with open(meta_file, 'r') as f:
                    meta_data = yaml.safe_load(f)
                    if meta_data:
                        roles_found.append(meta_data)
            else:
                os.makedirs(os.path.join(role_dir, 'meta'), exist_ok=True)
                with open(meta_file, 'w') as f:
                    yaml.dump({
                        'role_name': role_name,
                        'status': 'Unknown',
                        'short_description': 'No description provided',
                        'description': 'No description provided',
                        'long_description': 'No long description provided',
                        'dependencies': [],
                        'called_by': [],
                        'topic': '',
                        'subtopic': '',
                        'tags': [],
                        'tested': False,
                        'idempotent': False
                    }, f, default_flow_style=False, sort_keys=False)
    sorted_roles = sorted(roles_found, key=lambda x: x.get('role_name', '').lower())
    return sorted_roles

def prep_for_markdown(roles_found):
    markdown_data = []
    for role in roles_found:
        role_info = {
            'Role Name': f"`{role.get('role_name', 'N/A')}`",
            'Status': role.get('status', 'N/A'),
            'Short Description': role.get('short_description', 'N/A'),
            'Description': role.get('description', 'N/A'),
            'Long Description': role.get('long_description', 'N/A'),
            'Called By': ', '.join(role.get('called_by', [])) if 'called_by' in role and role['called_by'] else 'N/A',
            'Dependencies': ', '.join(role.get('dependencies', [])) if 'dependencies' in role and role['dependencies'] else 'N/A',
            'Topic': role.get('topic', 'N/A'),
            'Subtopic': role.get('subtopic', 'N/A'),
            'Tags': ', '.join(role.get('tags', [])) if 'tags' in role and role['tags'] else 'N/A',
            'Tested': role.get('tested', 'N/A'),
            'Idempotent': role.get('idempotent', 'N/A')
        }
        markdown_data.append(role_info)
    return markdown_table(markdown_data).set_params(row_sep='markdown', quote=False)

roles_info = get_ansible_roles('.')
markdown_output = prep_for_markdown(roles_info).get_markdown()
print(markdown_output)