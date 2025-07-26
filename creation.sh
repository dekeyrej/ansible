#!/usr/bin/env bash

echo "🌌 Ilúvatar awakens. Preparing the Song of Creation..."

# Check for vault.password
if [[ ! -f vault.password ]]; then
  echo "❌ The Secret Fire is missing (vault.password not found). Aborting."
  exit 1
fi

apt update
apt install -y git
git clone https://github.com/dekeyrej/ansible.git
mv vault.password ansible
cd ansible

echo "🧙‍♂️ Summoning the environment..."
python3 -m venv venv
source venv/bin/activate
pip install ansible proxmoxer requests

echo "⚡ Calling forth Manwë..."
ansible-playbook playbooks/the-creation-of-manwe.yaml

cd ..
rm -rf ansible
echo "✅ Ilúvatar rests. Manwë now walks the winds."
