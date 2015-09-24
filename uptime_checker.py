#!/usr/bin/env python

import subprocess as sp
import os
import re

# check the current uptime
output = sp.check_output("uptime", shell=True)

# check if a current record file exists and if not, make it.
# feel free to change this directory if you want to save this file elsewhere.
if os.path.isfile(os.path.expanduser("~/Documents/uptime_record.txt")) == False:
    record = open(os.path.expanduser("~/Documents/uptime_record.txt"), "w")
    record.write(output)
    record.close()

# maybe make all the rest of this an 'else' so that, if this is run for the first time, it won't re-make a file.
## look at current uptime record file to check if new uptime is greater
# find number of days in current record
check = open(os.path.expanduser("~/Documents/uptime_record.txt")).read()
check_string = re.findall("(?s)(?<=up).+?(?=day)", check)
check_number = ''.join(check_string)
actual_check_number = int(check_number)

# find current number of days
string = re.findall("(?s)(?<=up).+?(?=day)", output)
number = ''.join(string)
try: actual_number = int(number)
except ValueError:
    actual_number = 0

# if current number is greater than the record, write this new number to the record
if actual_number > actual_check_number:
    record = open(os.path.expanduser("~/Documents/uptime_record.txt"), "w")
    record.write(output)
    record.close()
