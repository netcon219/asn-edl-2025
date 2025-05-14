import requests

# List of ASNs
ASNS = ["AS44477"]  # Add more like: ["AS13335", "AS15169", "AS8075"]

def get_prefixes(asn):
    url = f"https://bgpview.io/api/asn/{asn}/prefixes"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        prefixes = r.json().get("data", {}).get("ipv4_prefixes", [])
        return [p["prefix"] for p in prefixes]
    except Exception as e:
        print(f"Error fetching {asn}: {e}")
        return []

# Write to blocklist.txt
with open("blocklist.txt", "w") as f:
    for asn in ASNS:
        for prefix in get_prefixes(asn):
            f.write(prefix + "\n")
