#!/usr/bin/env python3

# Add a 4th server and then print out each server and it's ip

hosts = [
        {"server": "North", "ip": "10.1.2.3"}, 
        {"server": "South", "ip": "10.4.5.6"}, 
        {"server": "West", "ip": "10.7.8.9"}
        ]
hosts.append({"server": "East", "ip": "10.10.11.12"})
print(hosts)

print(hosts[0]["server"], hosts[0]["ip"])

