import sys
import ipaddress
from panos.firewall import Firewall
from panos.network import EthernetInterface

def is_public_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return not ip_obj.is_private
    except ValueError:
        return False

def get_interface_ip(fw, interface_name):
    interface = EthernetInterface(interface_name)
    fw.add(interface)
    interface.refresh()
    return interface.ip

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python check_interface_ip.py <firewall_ip> <username> <password>")
        sys.exit(1)

    firewall_ip = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]

    fw = Firewall(firewall_ip, username, password)
    interface_name = 'ethernet1/2'
    interface_ip = get_interface_ip(fw, interface_name)

    if is_public_ip(interface_ip):
        print("public")
    else:
        print("private")
