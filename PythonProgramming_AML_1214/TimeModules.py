import time
import datetime
import calendar

currentgmtime = time.gmtime()
print("current GM time: ", currentgmtime)

currentEpochTime = time.time()
print("Epoch Time:", currentEpochTime)

currentCTime = time.ctime()
print("CTime     :", currentCTime)

start_time = time.time()
# time.sleep(5)
endTime = time.time()
duration = endTime - start_time
print("The process took: ", duration, "to complete!")

currentDateTime = datetime.datetime.now()
print("Date time: ", currentDateTime)

print(currentDateTime.strftime("%a"))
print(currentDateTime.strftime("%A"))
print(currentDateTime.strftime("%b"))
print(currentDateTime.strftime("%B"))
print(currentDateTime.strftime("%c"))
print(currentDateTime.strftime("%x"))
print(currentDateTime.strftime("%X"))

year = 2023
month = 3
print(calendar.month(year, month))
print(calendar.day_abbr)
