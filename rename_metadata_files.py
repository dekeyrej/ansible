import os

def get_ansible_roles(ansible_project_path):
    roles_path = os.path.join(ansible_project_path, 'roles')
    if not os.path.exists(roles_path):
        exit(1)

    for role_name in os.listdir(roles_path):
        role_dir = os.path.join(roles_path, role_name)
        if os.path.isdir(role_dir):
            main_file = os.path.join(role_dir, 'meta', 'main.yaml')
            data_file = os.path.join(role_dir, 'meta', 'data.yaml')
            if os.path.exists(main_file):
                os.rename(main_file, data_file)

roles_info = get_ansible_roles('.')