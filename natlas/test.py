#!/usr/bin/env python3

import networkscan
from nornir import InitNornir
from nornir_napalm.

# import nmap3
def write_file(self, file_type=0, filename="hosts.yaml"):
        """ Method to write a file with the list of the detected hosts """

if __name__=='__main__':
    mynetwork_name = "192.168.2.0/24"

    my_scan = networkscan.Networkscan(mynetwork_name)
    print("Network to scan: " + str(my_scan.network))
    print("Prefix to scan: " + str(my_scan.network.prefixlen))
    print("Number of hosts to scan: " + str(my_scan.nbr_host))
    my_scan.run()
    print("\nScanning hosts...")
    print("List of hosts found:")
    for host in my_scan.list_of_hosts_found:
        print(host)
    print("Number of hosts found: " + str(my_scan.nbr_host_found))
    res = my_scan.write_file()

    # Error while writting the file?
    if res:
        # Yes
        print("Write error with file " + my_scan.filename)
    else:
        # No error
        print("Data saved into file " + my_scan.filename)

    nr = InitNornir(config_file="config.yaml")
    # Run Nornir task (here getting the ARP table of the devices)
    result = nr.run(task=networking.napalm_get,name=" ARP table ",getters=["arp_table"])

    # Display the result
    print("Display ARP table of the network devices")
    print(result)
        
    # nmap = nmap3.Nmap()
    # nmap_scan = nmap.nmap_subnet_scan(mynetwork_name)
    # print(nmap_scan)

    # nm = nmap.PortScanner()
    # nmap_scan = nm.scan(mynetwork_name)
    # print(nmap_scan)
