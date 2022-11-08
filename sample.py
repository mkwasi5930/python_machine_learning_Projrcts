import time
import datetime
import pytz

timezone = pytz.utc
while True:

    print("executing")
    if (datetime.datetime.now(timezone).strftime("%A") == "Friday" and int(datetime.datetime.now(timezone).strftime("%H"))==23 and  int(datetime.datetime.now(timezone).strftime("%M"))>=45):
        print("my time to sleep")
        time.sleep(5)
    else:
        print(datetime.datetime.now(timezone).strftime("%A") == "Sunday")
        print(int(datetime.datetime.now(timezone).strftime("%H"))==11)
        print(datetime.datetime.now(timezone).strftime("%M"))
        print(datetime.datetime.now(timezone).strftime("%A"))
        print(datetime.datetime.now(timezone).strftime("%H"))
        time.sleep(5)