import os
import sys
from dotenv import load_dotenv
import ipaddress
import requests

def validate_ip_addr():
    if len(sys.argv) < 2:
        print('\nError: Missing an ipv4 or ipv6 address to check!\n')
        exit()
    ip_addr = str(sys.argv[1])
    if not ipaddress.ip_address(ip_addr) or ipaddress.ip_address(ip_addr).is_private:
        print('\nError: ' + ip_addr + ' is not a valid public ip address!\n')
        exit()
    return ip_addr

def validate_authentication():
    load_dotenv()
    if os.getenv('IPSTACK_ACCESS_KEY') == None:
        print('\nIPSTACK_ACCESS_KEY could not be found!\n')
        api_key = input('Please enter your IPSTACK_ACCESS_KEY...\n')
        if not api_key:
            print('\nError: Empty access key!\n')
            exit()
        envfile = open('.env', 'w')
        envfile.write('IPSTACK_ACCESS_KEY=' + api_key + '\n')
        envfile.close()
        print('\nIPSTACK_ACCESS_KEY Saved!\n')
        load_dotenv()
    access_key = os.getenv('IPSTACK_ACCESS_KEY')
    return access_key

def request_location(access_key, ip_addr):
    url = 'http://api.ipstack.com/' + ip_addr + '?access_key=' + access_key + '&fields=latitude,longitude'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        response.close()
        if 'error' in data:
            print('\nError: ' + data['error']['type'] + '\n')
            exit()
    except Exception as e:
        err = (str(e)).split('Caused by')[1]
        print('\nError:', err + '\n')
        exit()
    return data

def main():
    access_key = validate_authentication()
    ip_addr = validate_ip_addr()
    print(request_location(access_key, ip_addr))

main()