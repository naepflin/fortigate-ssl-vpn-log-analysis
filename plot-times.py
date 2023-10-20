import matplotlib.pyplot as plt
import matplotlib.dates

from datetime import datetime
from parselog import parse_log

log_data = parse_log()

actions = set([entry.get('action') for entry in log_data])

log_data = [entry for entry in log_data if entry.get('action') == "tunnel-up"]

users = set([entry.get('user') for entry in log_data])


for user in users:
    filter_key = "user"
    filter_value = user

    filtered_entries = [entry for entry in log_data if entry.get(filter_key) == filter_value]

    times = [int(entry.get("time")[:2]) for entry in filtered_entries]
    plt.figure()

    plt.hist(times, bins=24, edgecolor='k', range=(0,24), alpha=0.7)
    plt.axis([0,24,0,20])
    plt.title(filter_value)

plt.show()