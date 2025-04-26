import re
from datetime import datetime
import pandas as pd

# Read the original log file
with open("./ecflow.all", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Create dictionaries to store submit and complete times for each member
submit_times = {}
complete_times = {}

# Regular expression patterns for submit and complete logs
submit_pattern = r"LOG:\[(.*?)\]  submitted: .*?/(jrrfs_[^\s/]*)"
complete_pattern = r"LOG:\[(.*?)\]  complete: .*?/(jrrfs_[^\s/]*)"


# Extract and parse timestamps for each member
for line in lines:
    submit_match = re.search(submit_pattern, line)
    complete_match = re.search(complete_pattern, line)
    if submit_match:
        time_str = submit_match.group(1)
        member = f"{submit_match.group(2)}"
        submit_times[member] = datetime.strptime(time_str, "%H:%M:%S %d.%m.%Y")
    elif complete_match:
        time_str = complete_match.group(1)
        member = f"{complete_match.group(2)}"
        complete_times[member] = datetime.strptime(time_str, "%H:%M:%S %d.%m.%Y")

# Build a DataFrame and calculate the time difference in seconds
data = []
for member in sorted(set(submit_times) | set(complete_times)):
    submit_time = submit_times.get(member)
    complete_time = complete_times.get(member)
    time_diff_seconds = int((complete_time - submit_time).total_seconds()) if submit_time and complete_time else None
    data.append([member, submit_time, complete_time, time_diff_seconds])

pd.set_option("display.max_colwidth", None)
pd.set_option("display.width", 200)
result_df = pd.DataFrame(data, columns=["Member ID", "Submit Time", "Complete Time", "Time Difference (seconds)"])
result_df.to_csv("submission_times.csv", index=False)

column_widths = [30, 25, 25, 25]  # Adjust these as needed
separator = " " * 10

with open("submission_times.txt", "w", encoding="utf-8") as f:
    # Format and write header
    header = separator.join(col.ljust(width) for col, width in zip(result_df.columns, column_widths))
    f.write(header + "\n")

    # Format and write each row
    for _, row in result_df.iterrows():
        formatted_row = separator.join(
            str(value).ljust(width) if value is not None else "".ljust(width)
            for value, width in zip(row, column_widths)
        )
        f.write(formatted_row + "\n")

# Print the result or save to CSV file
print(result_df)
