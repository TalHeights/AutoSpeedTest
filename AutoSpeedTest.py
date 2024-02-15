import math
import speedtest

def Bytes_to_MegaBytes(size_bytes):
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f"{size} Mbps"

wifi = speedtest.Speedtest()

print("Getting dowload speed...")
download_speed = wifi.download()

print("Getting upload speed...")
upload_speed = wifi.upload()

print("Download: ", Bytes_to_MegaBytes(download_speed))
print("Upload: ", Bytes_to_MegaBytes(upload_speed))