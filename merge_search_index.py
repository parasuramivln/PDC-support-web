import json
import os
#-------------------------------------------------------------------------------
# Constants
#-------------------------------------------------------------------------------
SOFTWARE_MAIN="software-docs"
SUPPORT_MAIN="support-docs"
SOFTWARE_INDEX=SOFTWARE_MAIN+'/site/search/search_index.json'
SUPPORT_INDEX=SUPPORT_MAIN+'/site/search/search_index.json'
#-------------------------------------------------------------------------------
# Load search indices
with open(SOFTWARE_INDEX, 'r') as fp:
    index1 = json.load(fp)
with open(SUPPORT_INDEX, 'r') as fp:
    index2 = json.load(fp)
# Add prefixes to locations
for item in index1['docs']:
    item['location'] = f"../{SOFTWARE_MAIN}/{item['location']}"
for item in index2['docs']:
    item['location'] = f"../{SUPPORT_MAIN}/{item['location']}"
# Merge indices
merged_index = {
    "docs": index1['docs'] + index2['docs'],
    "config": index1['config']  # Assuming configs are the same
    }
# Save the merged index
with open(SOFTWARE_INDEX, 'w') as f:
    json.dump(merged_index, f, indent=4)
with open(SUPPORT_INDEX, 'w') as f:
    json.dump(merged_index, f, indent=4)
#-------------------------------------------------------------------------------
