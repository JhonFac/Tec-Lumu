def parse_bind_log(file_path):
    total_records = 0
    ip_occurrences = {}
    domain_occurrences = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()

            client_info = parts[6].split('@')[-1]
            client_ip = client_info.split('#')[0]
            ip_occurrences[client_ip] = ip_occurrences.get(client_ip, 0) + 1

            domain = line.split()[-3].strip('()')
            domain_occurrences[domain] = domain_occurrences.get(domain, 0) + 1

    print("Total records processed:", total_records)
    print("Total IP occurrences:", sum(ip_occurrences.values()))
    print("Total domain occurrences:", sum(domain_occurrences.values()))

    print("IP Occurrences:")
    total_ip_occurrences = sum(ip_occurrences.values())
    for ip, count in ip_occurrences.items():
        percentage = (count / total_ip_occurrences) * 100
        print(f"{ip}: {count} ({percentage:.2f}%)")

    print("\nDomain Occurrences:")
    total_domain_occurrences = sum(domain_occurrences.values())
    for domain, count in domain_occurrences.items():
        percentage = (count / total_domain_occurrences) * 100
        print(f"{domain}: {count} {percentage:.2f}%")

bind_log_file = 'queries'
parse_bind_log(bind_log_file)
