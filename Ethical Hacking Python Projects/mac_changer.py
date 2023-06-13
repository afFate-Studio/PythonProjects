#!/usr/bin/env python

import subprocess
import optparse
import re

# function used to get the current mac address
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    search_results = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    mac_address = search_results.group(0)
    if mac_address:
        return mac_address
    else:
        print("[-] Could not read MAC address")

# function used to get user arguments
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface selection ex. eth0")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac Address value ex. 00:00:00:00:00:00")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Enter a valid interface. Use -h or --help for more information.")
    elif not options.new_mac:
        parser.error("[-] Enter a valid mac address. Use -h or --help for more information.")
    else:
        return options

# function used to change the mac address
def change_mac(interface, new_mac):
    print("--------------------------------------------------------------------------------")
    print("\n\t[+] Changing Mac address for {0} to {1}\n".format(interface, new_mac))
    print("--------------------------------------------------------------------------------")

    # safe version of the subprocess.call function, cannot be hijacked
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface])

# function used to revert to original mac address
def revert_mac(interface, original_mac_address):
    print("--------------------------------------------------------------------------------")
    print("\n\t[+] Reverting the Mac address to the original value {}\n".format(original_mac_address))
    print("--------------------------------------------------------------------------------")


    # replace to original mac address then call ifconfig interface
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", original_mac_address])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface])


# process users given values
options = get_arguments()

# store original mac address to restore settings
original_mac_address = get_current_mac(options.interface)

# change mac address to user given value
change_mac(options.interface, options.new_mac)

# used to check if mac address changed
current_mac_address = get_current_mac(options.interface)
if current_mac_address == options.new_mac:
    print("--------------------------------------------------------------------------------")
    print("\t[+] The MAC Address has been successfully changed to {}".format(current_mac_address))
    print("--------------------------------------------------------------------------------")

else:
    print("--------------------------------------------------------------------------------")
    print("\t[-] The MAC Address has not changed.")
    print("--------------------------------------------------------------------------------")

# revert mac address to original value
#revert_mac(options.interface, original_mac_address)
