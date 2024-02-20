import math
import speedtest
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def Bytes_to_MegaBytes(size_bytes): # this function converting from bytes to megabytes.
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f"{size} Mbps"


# Test loop:
def do_task(wifi, ServerValue):
    
    print("Performing task...")

    print(f"Current time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    wifi.get_servers(servers=[ServerValue.get('id')]) # For specipic server replace "ServerValue.get('id')" to other ID.
    print("Testing with: " + ServerValue.get('sponsor'))

    print("Getting download speed...")
    download_speed = wifi.download() # Getting download speed.

    print("Getting upload speed...")
    upload_speed = wifi.upload() # Getting upload speed.

    print("Download: ", Bytes_to_MegaBytes(download_speed))
    print("Upload: ", Bytes_to_MegaBytes(upload_speed))


# Setup:
def schedule_task():
    
    print("Initializes code...")
    
    wifi = speedtest.Speedtest()

    ServerValue = wifi.get_best_server() # Store best server in "ServerValue".

    print('Best server by latency is: ' + ServerValue.get('sponsor') + ", Location: " + ServerValue.get('name') + ", ID: " + ServerValue.get('id') + ".")

    scheduler = BlockingScheduler()

    scheduler.add_job(do_task, 'cron', args=[wifi, ServerValue], minute='*/5') # Schedule the task to run every 5 minute using cron expression.

    print("Scheduler started.")

    try: # Start the scheduler.
        scheduler.start()
    except KeyboardInterrupt:
        pass



if __name__ == "__main__":
    schedule_task()