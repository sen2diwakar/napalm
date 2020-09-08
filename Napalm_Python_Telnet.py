from napalm import get_network_driver
import json
from datetime import datetime
import getpass
import os
import sys
import time
import re
import telnetlib



class LoginThroughTelnet:

    def FetchArpTable(self):
        try:
            print("Logging to Telnet device")
            driver = get_network_driver('ios')
            optional_args = {'port': '23', 'transport': 'telnet', 'secret':'please enter your secret password here(remove the argument if not required)'}
            device = driver('enter ip address here', 'enter username here', 'enter password here', optional_args=optional_args)
            print("open connection")
            device.open()
            print("Logging completed")
            output = device.hostname
            print("device hostname is: ",output,"\n")
            output = device.get_arp_table()
            print("Arp table output is",json.dumps(output, indent=2))

        except:
            raise RuntimeError("Napalm script failed to execute")

BGP = LoginThroughTelnet()

def connect_to_device():

    BGP.FetchArpTable()
