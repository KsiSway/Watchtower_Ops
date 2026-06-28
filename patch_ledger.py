import csv

intel = {
    '192.168.68.110': {'Hostname': 'OptiPlex_3050_Host', 'MAC': '14-B3-1F-07-95-77', 'Vendor': 'Dell'},
    '192.168.68.109': {'Hostname': 'S25_Edge_Commander', 'MAC': 'C4-EF-3D-92-BA-9B', 'Vendor': 'Samsung'},
    '192.168.68.112': {'Hostname': 'Tab_A8_Rooted', 'MAC': '6A-68-CE-46-65-79', 'Vendor': 'Samsung'},
    '192.168.68.113': {'Hostname': 'Samsung_SmartMonitor', 'MAC': 'F2-2C-30-30-63-60', 'Vendor': 'Samsung'},
    '192.168.68.104': {'Hostname': 'Xbox_Series_S', 'MAC': 'D8-E2-DF-6D-94-D8', 'Vendor': 'Microsoft'}
}

file_path = 'D:\\Watchtower_Ops\\Watchtower_Final_Baseline.csv'
rows = []
with open(file_path, 'r', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        ip = row['IP']
        if ip in intel:
            row['Hostname'] = intel[ip]['Hostname']
            row['MAC'] = intel[ip]['MAC']
            row['Vendor'] = intel[ip]['Vendor']
        rows.append(row)

with open(file_path, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print('\n[*] Ledger patched with known Exocortex intelligence.')
