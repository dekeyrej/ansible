import os
import json
import yaml
from py_markdown_table.markdown_table import markdown_table

with open('monolithic_table.json', 'r') as file:
    monolithic_table = json.load(file)

def get_ansible_roles(ansible_project_path):
    roles_updated = 0
    roles_path = os.path.join(ansible_project_path, 'roles')
    if not os.path.exists(roles_path):
        exit(1)
    roles_found = []

    update_keys = ['long_description', 'dependencies', 'called_by', 'tested', 'idempotent']
    keymap = {
        'role_name': 'Role Name',
        'long_description': 'Description',
        'dependencies': 'Depends On',
        'called_by': 'Called In',
        'tested': 'Tested',
        'idempotent': 'Idempotent'
    }
    
    for role_name in os.listdir(roles_path):
        role_dir = os.path.join(roles_path, role_name)
        if os.path.isdir(role_dir):
            main_file = os.path.join(role_dir, 'meta', 'data.yaml')
            if os.path.exists(main_file):
                with open(main_file, 'r') as f:
                    main_data = yaml.safe_load(f)
                if monolithic_table.get(role_name):
                    roles_updated += 1
                    for k in update_keys:
                        if keymap[k] in monolithic_table[role_name]:
                            main_data[k] = monolithic_table[role_name][keymap[k]]
                            if k == 'tested' and main_data[k] == 'Tested':
                                main_data[k] = '✅ Yes'
                            elif k == 'idempotent' and main_data[k] == 'Yes':
                                main_data[k] = '✅ Full'
                roles_found.append(main_data)
    sorted_roles = sorted(roles_found, key=lambda x: x.get('role_name', '').lower())
    # print(f"Roles updated: {roles_updated}")
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
print("Roles found:\n", json.dumps(roles_info, indent=2))
# markdown_output = prep_for_markdown(roles_info).get_markdown()
# print(markdown_output)