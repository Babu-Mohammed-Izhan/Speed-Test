#  This is a speed test program written in python 3
#  For this program you have to have python 3 installed in your computer
# 
#  You will also need to pip install speedtest-cli form command prompt 
#     For this you will need to go to command prompt and write
#     py -m pip install speedtest-cli  
#             or
#     python -m pip install speedtest-cli

import speedtest as st


def get_new_speeds():
    speed_test = st.Speedtest()
    speed_test.get_best_server()

    # Get ping (miliseconds)
    ping = speed_test.results.ping
    
    # Perform download and upload speed tests (bits per second)
    download = speed_test.download()
    upload = speed_test.upload()

    # Convert download and upload speeds to megabits per second
    download_mbs = round(download / (10**6), 2)
    upload_mbs = round(upload / (10**6), 2)

    return ("Ping: "+str(ping),"Download: " +str(download_mbs),"Upload: "+str(upload_mbs))

speed= get_new_speeds()

print(speed)