import argparse
import logging
import sys
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import LiteralScalarString
from ruamel.yaml.comments import TaggedScalar
from ansible.parsing.vault import VaultLib, VaultSecret
from ansible.constants import DEFAULT_VAULT_ID_MATCH

logging.basicConfig(level=logging.INFO)

# def encrypt_keys_recursively(data, keys_to_encrypt, vault):
#     if isinstance(data, dict):
#         return {
#             k: encrypt_keys_recursively(v, keys_to_encrypt, vault) if isinstance(v, (dict, list))
#             else ansible_vault_encrypt_str(vault, v) if k in keys_to_encrypt
#             else v
#             for k, v in data.items()
#         }
#     elif isinstance(data, list):
#         return [encrypt_keys_recursively(item, keys_to_encrypt, vault) for item in data]
#     return data

def main():

    def ansible_vault_encrypt_str(vault, value_str) -> str:
        try:
            encrypted_value = vault.encrypt(value_str)
            return encrypted_value.decode('utf-8')  # Decode bytes to string
        except Exception as e:
            logging.error(f"Error encrypting vault: {e}")
            return value_str
        
    def ansible_vault_decrypt_str(vault, value_str) -> str:
        try:
            decrypted_value = vault.decrypt(value_str)
            return decrypted_value.decode('utf-8')  # Decode bytes to string
        except Exception as e:
            logging.error(f"Error decrypting vault: {e}")
            return value_str

    def vault_tagged_scalar(vault, value_str):
        encrypted_value = ansible_vault_encrypt_str(vault, value_str)
        if encrypted_value.startswith('$ANSIBLE_VAULT;'):
            return TaggedScalar(LiteralScalarString(encrypted_value), tag='!vault', style='|')
        else:
            return encrypted_value
        
    def find_ansible_config():
        import os
        # look for ansible.cfg in ./ansible.cfg, ~/.ansible.cfg, /etc/ansible/ansible.cfg
        config_paths = [
            './ansible.cfg',
            os.path.expanduser('~/.ansible.cfg'),
            '/etc/ansible/ansible.cfg'
        ]
        for path in config_paths:
            if os.path.exists(path):
                logging.debug(f"Found Ansible config at: {path}")
                return path
        logging.warning("No Ansible config found.")
        return None

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.default_flow_style = False
    ap = argparse.ArgumentParser(description="Selectively encrypt sensitive variables")
    ap.add_argument("command", choices=["encrypt", "decrypt", "view"], help="Command to execute")  # maybe "edit" in the future
    ap.add_argument("input", help="Path to input YAML file")
    ap.add_argument("--output", nargs="?", default=None, help="Path to output YAML file (optional), defaults to input file, will clobber without warning")
    ap.add_argument("--vault-password-file", default=None, help="Path to vault password file")
    ap.add_argument("--keys", nargs="+", default=[], help="Keys to encrypt")
    ap.add_argument("--dry-run", action="store_true", help="Show changes without writing to file")
    args = ap.parse_args()
    command = args.command
    input_file = args.input
    output_file = args.output or input_file
    password_file_path = args.vault_password_file
    keys_to_encrypt = args.keys
    dry_run = args.dry_run

    # read or find password from file, if we find it initialize the vault, else exit
    logging.debug(f"Using vault password file: {password_file_path}")
    if not password_file_path:
        config_file_path = find_ansible_config()
        if config_file_path:
            import configparser
            config = configparser.ConfigParser()
            config.read(config_file_path)
            password_file_path = config.get("defaults", "vault_password_file", fallback=password_file_path)
        else:
            logging.error("No Ansible config found.")
            sys.exit(1)
    try:
        with open(password_file_path, 'r') as pf:
            vault_password = pf.read().strip()
    except FileNotFoundError:
        logging.error(f"File not found: {password_file_path}")
        sys.exit(1)
    vault = VaultLib([(DEFAULT_VAULT_ID_MATCH, VaultSecret(vault_password.encode()))])
    
    # read the input file, or exit
    try:
        with open(input_file, 'r') as f:
            vars = yaml.load(f)
    except yaml.YAMLError as e:
        logging.error(f"Error loading YAML file: {e}, one or more values is (probably) already encrypted")
        sys.exit(1)
    except FileNotFoundError:
        logging.error(f"File not found: {input_file}")
        sys.exit(1)

    # perform the right logic for the command
    if command == 'encrypt':
        keys_to_encrypt = args.keys or vars.get('encrypted_keys', [])
        if keys_to_encrypt:
            for key in keys_to_encrypt:
                if key in vars:
                    vars[key] = vault_tagged_scalar(vault, vars[key])
                else:
                    logging.warning(f"Key not found for encryption: {key}")
            if dry_run:
                logging.info("Dry run mode: changes will not be written to file.")
                yaml.dump(vars, sys.stdout)
            else:
                with open(output_file, "w") as f:
                    yaml.dump(vars, f)
                logging.info(f"Changes written to {output_file}")
    elif command == 'decrypt':
        keys_to_encrypt = args.keys or vars.get('encrypted_keys', [])
        if keys_to_encrypt:
            for k, v in vars.items():
                if isinstance(v, TaggedScalar):
                    vars[k] = ansible_vault_decrypt_str(vault, v)
            with open(output_file, 'w') as df:
                yaml.dump(vars, df)
        else:
            encrypted_keys = []
            for k, v in vars.items():
                if isinstance(v, TaggedScalar):
                    encrypted_keys.append(k)
                    vars[k] = ansible_vault_decrypt_str(vault, v)
            vars['encrypted_keys'] = encrypted_keys
            with open(output_file, 'w') as df:
                yaml.dump(vars, df)
    elif command == 'view':
        for k, v in vars.items():
            if isinstance(v, TaggedScalar):
                vars[k] = ansible_vault_decrypt_str(vault, v)
        yaml.dump(vars, sys.stdout)

if __name__ == "__main__":
    main()
