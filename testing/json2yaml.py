import json
import yaml

with open('/home/ubuntu/cluster_recipe/deployment/secrets.json','r') as f:
    data = json.load(f)
    
print(yaml.dump(data, default_flow_style=False))
