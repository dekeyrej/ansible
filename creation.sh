#!/usr/bin/env bash

echo "🌌 Ilúvatar awakens. Preparing the Song of Creation..."

# Check for vault.password
if [[ ! -f vault.password ]]; then
  echo "❌ The Secret Fire is missing (vault.password not found). Aborting."
  exit 1
fi

# make sure .profile appends ~/.local/bin to the path
if ! grep -q "/root/.local/bin" /root/.profile; then
  echo "export PATH=\$PATH:/root/.local/bin" >> /root/.profile
fi

if [[ ! -d /root/.local/bin ]]; then
  echo "🧙‍♂️ Summoning the environment..."
  python3 -m venv /root/.local
  source .profile
  # source /root/.local/bin/activate
  pip install ansible proxmoxer requests
fi

apt update
apt install -y git
git clone https://github.com/dekeyrej/ansible.git
mv vault.password ansible
cd ansible

echo "⚡ Calling forth Manwë..."
ansible-playbook playbooks/the-creation-of-manwe.yaml

cd ..
rm -rf ansible
echo "✅ Ilúvatar rests. Manwë now walks the winds."
