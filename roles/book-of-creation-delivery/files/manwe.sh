#!/usr/bin/env bash

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