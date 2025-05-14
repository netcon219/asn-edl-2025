import requests

# List of ASNs to include (no "AS" prefix needed)
ASNS = ["44477"]  

def get_prefixes(asn):
    url = f"https://ipinfo.io/AS{asn}/routes"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.text.strip().splitlines()
    except Exception as e:
        print(f"Error fetching AS{asn}: {e}")
        return []

# Write to blocklist.txt
with open("blocklist.txt", "w") as f:
    for asn in ASNS:
        for prefix in get_prefixes(asn):
            f.write(prefix + "\n")
