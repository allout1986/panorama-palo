from panos import panorama
from panos.firewall import Firewall
from panos.objects import NatRule

class PanoramaAPI:
    def __init__(self, host, username, password):
        self.panorama = panorama.Panorama(hostname=host, username=username, password=password)

    def get_device_groups(self):
        device_groups = self.panorama.refresh_devices()
        for dg in device_groups:
            if isinstance(dg, Firewall):
                print(f"Device Group: {dg.hostname}")

    def get_nat_configurations(self):
        # Assuming we're working with a specific device group
        # Replace 'device_group_name' with your device group name
        device_group = panorama.DeviceGroup('device_group_name')
        self.panorama.add(device_group)

        # Fetch NAT rules
        nat_rules = device_group.findall(NatRule)
        for rule in nat_rules:
            print(f"NAT Rule: {rule.name}")

# Usage
host = 'PANORAMA_HOST_IP'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
panorama_api = PanoramaAPI(host, username, password)

# Display device groups
panorama_api.get_device_groups()

# Display NAT configurations
panorama_api.get_nat_configurations()
