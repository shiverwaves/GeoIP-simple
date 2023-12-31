# GeoIP-simple

This is a simple REST implementation consuming [IPstack's Standard Lookup API](https://ipstack.com/documentation#standard) that performs IP Geolocation.
The application is command line based, it takes a single argument (any valid public ipv4 or ipv6 address) 
and then returns a python dictionary (JSON) of latitude and longitude coordinates for a given public ip address.


# How to use

IPstack requires an api "access key" in order to authenticate to their services. 
If you do not have an IP stack API access key, you can sign up for one free [here.](https://ipstack.com/signup/free)

You will need to install the prerequisite python packages. This can be easily achieved using "pip3" and the requirements.txt file provided.
On the first run of the application, it will check to see if an IPSTACK_ACCESS_KEY environment variable is present in the local .env file.
This should be present in the current working directory of the application.
If one is not found, you will be prompted for your IPSTACK_ACCESS_KEY and it will be saved in a new .env file.
Any subsequent runs of the application will always will check for the .env file and IPSTACK_ACCESS_KEY during runtime.

***NOTE if running in a docker container, the process having to input API keys may need to be performed each time the container is reloaded.
It is possible to run the container with a persistent volume to prevent having to perform this procedure. 
This has not been tested, and may require some minor tweaks with the .env file [and where its stored]***

***1. Clone the repo***

   git clone GeoIP-simple

***2. Navigate into the repo***
   
   cd GeoIP-simple

***3. Install the prerequisite python packages***
   
   pip3 install -r requirements.txt

***4. Execute python application***
   
   python3 geoip-simple.py 4.4.4.4

# Response Example

{'longitude': -157.81410217285156, 'latitude': 21.32217025756836}


# How to run in docker container

***1. Clone the repo***

   git clone GeoIP-simple

***2. Execute the build process***

   docker build -t geo-ip-simple --rm .

***3. Run the container in interactive mode***

   docker run -it --rm geo-ip-simple

***4. Execute the python application (inside the container)***

   python3 geoip-simple.py 4.4.4.4
