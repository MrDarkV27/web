import requests
import time

def make_request():
    url = 'https://amodz.online'  # Replace with the desired URL

    # Send GET request
    response = requests.get(url)
   

while True:
    make_request()
    time.sleep(001)  # Delay for 200 seconds
