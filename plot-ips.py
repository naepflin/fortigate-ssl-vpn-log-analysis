from parselog import parse_log

log_data = parse_log()

# actions = set([entry.get('action') for entry in log_data])

log_data = [entry for entry in log_data if entry.get('action') == "tunnel-up"]

users = set([entry.get('user') for entry in log_data])


for user in users:
    filter_key = "user"
    filter_value = user

    filtered_entries = [entry for entry in log_data if entry.get(filter_key) == filter_value]
    ips = set(['.'.join(entry.get("remip").split(".")[:-1]) + ".0" for entry in filtered_entries])
    for ip in ips:
        print(ip)

