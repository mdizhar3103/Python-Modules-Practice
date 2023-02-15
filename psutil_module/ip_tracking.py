import ipapi 
import webbrowser
import socket
import sys, time 
from ipaddress import ip_address
from requests import get 

# pip install ipapi ipaddress 

lookup = "www.yahoo.com"

# Perform name lookup
try:
    ip  = str(ip_address(lookup))
except ValueError:
    print("Looking up Name")
    ip = socket.gethostbyname(lookup)
except Exception as e:
    print(e)
    sys.exit()

# Perform location lookup
try:
    print("Lookup location data")
    location_data = ipapi.location(ip)  # result='latitude'
except Exception as e:
    print(e)
else:
    print(location_data)

    latitude = location_data['latitude']
    longitude = location_data['longitude']

    # location_query = "https://www.google.com/maps/search/?api=1&query" + str(latitude) + "%2C" + str(longitude) 
    # webbrowser.open(location_query, new=2)
