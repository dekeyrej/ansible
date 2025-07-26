> ## “In the beginning, Ilúvatar sang the world into being. From his song came Manwë, and from Manwë came the shaping of Arda...”

## TL;DR
This is a modular Ansible suite for provisioning a Tolkien-themed homelab. Each host represents a character or realm, and each playbook is a chapter in the shaping of Arda.

## 📚 Table of Contents
- [🌌 creation.sh on Ilúvatar](#-creationsh-on-ilúvatar-primordial-setup)
- [🗂️ Structure: Thematic & Functional](#️-structure-thematic--functional)
- [🧙‍♂️ Modular Execution](#️-modular-execution)

## 🏰 Legend of Hosts

| Hostname      | Role / Identity       | Description                                  |
|---------------|------------------------|----------------------------------------------|
| Ilúvatar      | Creator                | Runs `creation.sh`, initiates the world      |
| Manwë         | Orchestrator           | Runs `manwe.sh`, controls the winds of setup |
| Celebrimbor   | Builder                | Crafts container images and artifacts        |
| Moria         | Vault                  | Stores secrets in the depths                 |
| Aragorn       | Kubernetes node        | Part of the Fellowship cluster               |
| Legolas       | Kubernetes node        | Agile and swift in orchestration             |
| Gimli         | Kubernetes node        | Sturdy and dependable                        |
| Gandalf       | MagicMirror2           | Offers wisdom and visibility                 |
| Galadriel     | Open-WebUI + Ollama      | Sees beyond the veil                         |
| Bombadil      | Self-contained node    | Lives outside the orchestration, yet vital for testing  |

## 🌌 creation.sh on Ilúvatar (Primordial Setup)
This script sets the stage, prepares the environment, and invokes the first playbook to bring Manwë into being.
```bash
#!/usr/bin/env bash

echo "🌌 Ilúvatar awakens. Preparing the Song of Creation..."

if [[ ! -f vault.password ]]; then
  echo "❌ The Secret Fire is missing (vault.password not found). Aborting."
  exit 1
fi

apt update
apt install -y git
git clone https://github.com/dekeyrej/ansible.git    # this is where all of these playbooks and roles are hosted
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
```

note: create a `vault.password` file to auto-decrypt your encrypted files, **before** running `creation.sh`

## 🗂️ Structure: Thematic & Functional
| Playbook | Purpose / Role | 
|---|---|
| the-creation-of-manwe.yaml | Provisioning the control node (Manwë) with Certificate Authority, initial setup from Ilúvatar | 
| the-delving-of-moria.yaml | Provisions vault container (Moria)| 
| the-birth-of-celebrimbor.yaml | Provisions Builder VM setup for local image crafting (Celebrimbor) | 
| the-forming-of-the-fellowship.yaml | Multi-node Kubernetes [MicroK8S] cluster (Aragorn, Legolas, Gimli) | 
| the-coming-of-stormcrow.yaml | Provisions container running MagicMirror2 (Gandalf) |
| the-vision-in-lothlorien.yaml | Provisions Open-WebUI container for running local LLMs (Galadriel) | 
| the-story-of-tom-bombadil.yaml | Provisions VM as single-node, self-contained certificate authority, vault, Kubernetes cluster for testing (Bombadil) | 


## 🧙‍♂️ Modular Execution:

`manwe.sh` a phase-driven orchestrator:
```bash
#!/usr/bin/env bash

source ~/ansible/venv/bin/activate

declare -a chapters=(
  "the-delving-of-moria.yaml"
  "the-birth-of-celebrimbor.yaml"
  "the-forming-of-the-fellowship.yaml"
  "the-coming-of-stormcrow.yaml"
  "the-vision-in-lothlorien.yaml"
  "the-story-of-tom-bombadil.yaml"
)

for chapter in "${chapters[@]}"; do
  if ! ansible-playbook "playbooks/$chapter"; then
    echo "❌ Failed to read $chapter. The winds falter."
    exit 1
  fi
  echo "📖 Reading $chapter..."
  ansible-playbook "playbooks/$chapter" | tee -a ~/arda.log
done

echo "🌈 All chapters complete. Arda is shaped."
```