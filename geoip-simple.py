import os
import sys
from dotenv import load_dotenv

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


def main():
    access_key = validate_authentication()
    print(access_key)

main()