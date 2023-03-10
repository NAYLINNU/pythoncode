#!usr/bin/env python
import subprocess
import optparse
import re
#that is for python3
#if u don't know how to do this, you can call -h option
# python3 mac_changer_all_way_py3.py -h
#run command= python3 mac_changer_all_way_py3.py -i wlan0 -m 00:11:11:11:11:11
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
        # erro comand = python3 mac_changer_using_condition.py -m 00:11:22:33:44:44
    elif not options.new_mac:
        parser.error("[-] Please specify new mac, use --help for more info")
        # erro comand = python3 mac_changer_using_condition.py -i wlan0 (or) etho
    return options
def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")
options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC " + str(current_mac))

change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")

