def parse_log():
    log_data = []

    with open("memory-event-vpn-2023_10_04.log") as logfile:
        for line in logfile:
            line = line.strip()
            log_entry = {}

            while len(line) != 0:
                key, _, line = line.partition("=")
                key = key.strip()
                
                if line.startswith('"'):
                    _, value, line = line.split('"', 2)
                else:
                    value, _, line = line.partition(" ")

                log_entry[key] = value
            log_data.append(log_entry)
    return log_data
