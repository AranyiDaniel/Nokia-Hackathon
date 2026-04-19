import json
import re
from pathlib import Path


def parse_ipconfig_file(file_path):
    try:
        content = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        content = file_path.read_text(encoding="utf-16")

    adapters = []
    current_adapter = None
    last_key = None

    mapping = {
        "Description": "description",
        "Physical Address": "physical_address",
        "DHCP Enabled": "dhcp_enabled",
        "IPv4 Address": "ipv4_address",
        "Autoconfiguration IPv4 Address": "ipv4_address",
        "Subnet Mask": "subnet_mask",
        "Default Gateway": "default_gateway",
        "DNS Servers": "dns_servers"
    }

    lines = content.splitlines()

    for line in lines:
        stripped = line.strip()
        
        if line and not line.startswith(" ") and line.endswith(":"):
            if "adapter" in line.lower():
                current_adapter = {
                    "adapter_name": line.replace(":", "").strip(),
                    "description": "",
                    "physical_address": "",
                    "dhcp_enabled": "",
                    "ipv4_address": "",
                    "subnet_mask": "",
                    "default_gateway": "",
                    "dns_servers": []
                }
                adapters.append(current_adapter)
                last_key = None
                continue

        if current_adapter and ":" in line:
            key_raw, value_raw = line.split(":", 1)
            clean_key = key_raw.replace(".", "").strip()
            clean_value = value_raw.split("(")[0].strip()

            if clean_key in mapping:
                json_key = mapping[clean_key]
                if json_key == "dns_servers":
                    if clean_value: current_adapter[json_key].append(clean_value)
                else:
                    current_adapter[json_key] = clean_value
                last_key = json_key
        
        elif current_adapter and last_key and stripped and ":" not in line:
            if last_key == "dns_servers":
                current_adapter[last_key].append(stripped)
            elif last_key == "default_gateway" and not current_adapter[last_key]:
                current_adapter[last_key] = stripped

    return adapters






def main():
    all_results = []
    
    for file_path in sorted(Path(".").glob("*.txt")):
        
        file_data = {
            "file_name": file_path.name,
            "adapters": parse_ipconfig_file(file_path)
        }
        all_results.append(file_data)

    output_path = Path("network_config.json")
    with output_path.open("w", encoding="utf-8") as json_file:
        json_string = json.dumps(all_results, indent=2, ensure_ascii=False)
        
        print(json_string)
        
        json_file.write(json_string)

        

if __name__ == "__main__":
    main()
