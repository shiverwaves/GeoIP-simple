import os
import sys
from dotenv import load_dotenv
import ipaddress

def validate_authentication():
    load_dotenv()
    if os.getenv('IPSTACK_ACCESS_KEY') == None: # check if access key exists in .env file
        print('\nIPSTACK_ACCESS_KEY could not be found!\n')
        api_key = input('Please enter your IPSTACK_ACCESS_KEY...\n')
        if not api_key:
            print('\nError: Empty access key!\n')
            exit()
        envfile = open('.env', 'w') # create an .env file if it does not exist.
        envfile.write('IPSTACK_ACCESS_KEY=' + api_key + '\n')
        envfile.close()
        print('\nIPSTACK_ACCESS_KEY Saved!\n')
        load_dotenv()
    access_key = os.getenv('IPSTACK_ACCESS_KEY')
    return access_key

def validate_ip_addr():
    # check for argv input
    if len(sys.argv) < 2:
        print('\nError: Missing an ipv4 or ipv6 address to check!\n')
        exit()
    ip_addr = str(sys.argv[1]) # only read the first arg.
    # perform input validation on the ipv4 or ipv6 address.
    if not ipaddress.ip_address(ip_addr) or ipaddress.ip_address(ip_addr).is_private:
        print('\nError: ' + ip_addr + ' is not a valid public ip address!\n')
        exit()
    return ip_addr

def main():
    access_key = validate_authentication()
    #print(access_key)
    ip_addr = validate_ip_addr()
    print(ip_addr)

main()