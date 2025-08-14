import pandas as pd
import re

# Step 1: Read the file
with open("node.txt", "r") as file:
    lines = file.readlines()

# Step 2: Extract jrrfs_* and number after select=
results = []
for line in lines:
    match = re.search(r'(jrrfs_[^:\s]+).*?select=(\d+)', line)
    if match:
        member_id = match.group(1).replace('.ecf', '')  # Step 3: Remove '.ecf'
        select_value = int(match.group(2))
        results.append((member_id, select_value))

# Step 4: Convert to DataFrame
node_summary_df = pd.DataFrame(results, columns=['Member ID', 'Select Value'])

# Optional: print or save
print(node_summary_df.head())  # Preview
node_summary_df.to_csv("node.csv", index=False)

