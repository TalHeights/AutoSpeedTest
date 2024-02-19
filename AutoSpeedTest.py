import math
import speedtest

# Setup:
def Bytes_to_MegaBytes(size_bytes): # this function converting from bytes to megabytes.
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f"{size} Mbps"

wifi = speedtest.Speedtest()

ServerValue = wifi.get_best_server() # Store best server in "ServerValue".

print('Best server by latency is: ' + ServerValue.get('sponsor') + ", Location: " + ServerValue.get('name') + ", ID: " + ServerValue.get('id') + ".")

# Test loop:
wifi.get_servers(servers=[ServerValue.get('id')]) # For specipic server replace "ServerValue.get('id')" to other ID.
print("Testing with: " + ServerValue.get('sponsor'))

print("Getting download speed...")
download_speed = wifi.download() # Getting download speed.

print("Getting upload speed...")
upload_speed = wifi.upload() # Getting upload speed.

print("Download: ", Bytes_to_MegaBytes(download_speed))
print("Upload: ", Bytes_to_MegaBytes(upload_speed))