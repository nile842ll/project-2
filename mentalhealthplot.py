import json
import matplotlib.pyplot as plt
from collections import defaultdict

# Load JSON file
with open("mental-healthcare-dataset.json", encoding="utf-8") as f:
    data = json.load(f)

rows = data["data"]

# Dictionary: {state: list of percentages}
state_values = defaultdict(list)

for row in rows:
    state = row[10]
    value = row[17]

    if state != "United States" and value:
        try:
            percent = float(value)
            state_values[state].append(percent)
        except ValueError:
            continue

# Calculate average per state
state_averages = {
    state: sum(vals) / len(vals)
    for state, vals in state_values.items()
}

# Sort by value
sorted_items = sorted(state_averages.items(), key=lambda x: x[1], reverse=True)

# Plot
states = [item[0] for item in sorted_items]
values = [item[1] for item in sorted_items]

plt.figure(figsize=(15, 6))
plt.bar(states, values, color="teal")
plt.xticks(rotation=90)
plt.ylabel("Average % on Prescription Meds")
plt.title("Mental Health Prescription Usage by State")
plt.tight_layout()
plt.savefig("mental_health_bar_fixed.png")
plt.show()
