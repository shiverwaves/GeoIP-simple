# GeoIP-simple

This is a simple REST implementation consuming [IPstack's Standard Lookup API](https://ipstack.com/documentation#standard) that performs IP Geolocation.
The application is command line based, it takes a single argument (any valid public ipv4 or ipv6 address).
It then returns a python dictionary (JSON) of latitude and longitude coordinates for a given public ip address.


# How to use

IPstack requires an api "access key" in order to authenticate to their services. 
If you do not have an IP stack API access key, you can sign up for one free [here.](https://ipstack.com/signup/free)

On the first run of the application, it will check to see if an IPSTACK_ACCESS_KEY environment variable is present in the local .env file.
This should be present in the current working directory of the application.
If one is not found, you will be prompted for your IPSTACK_ACCESS_KEY and it will be saved in a new .env file.
Any subsequent runs of the application will always will check for the .env file and value for IPSTACK_ACCESS_KEY during runtime.

# Example:

python3 geoip-simple.py 4.4.4.4

# Response Example:

{'longitude': -157.81410217285156, 'latitude': 21.32217025756836}

# How to run in docker container
