import subprocess as sp
import os
import re

# check the current uptime
output = sp.check_output("uptime", shell=True)

# check if a current record file exists and if not, make it
if os.path.isfile(os.path.expanduser("~/documents/uptime_record.txt")) == False:
    record = open(os.path.expanduser("~/documents/uptime_record.txt"), "w")
    record.close()


## look at current uptime record file to check if new uptime is greater
# find number of days in current record
check = open(os.path.expanduser("~/documents/uptime_record.txt")).read()
check_string = re.findall("(?s)(?<=up).+?(?=days)", check)
check_number = ''.join(check_string)
actual_check_number = int(check_number)

# find current number of days
string = re.findall("(?s)(?<=up).+?(?=days)", output)
number = ''.join(string)
actual_number = int(number)

# if current number is greater than the record, write this new number to the record
if number > check_number:
    record = open(os.path.expanduser("~/documents/uptime_record.txt"), "w")
    record.write(output)
    record.close()







## all this is junk from testing but I am keeping it here for now.
# make something for if uptime record file doesn't exist, create it
# this line allows the use of ~
#open(os.path.expanduser("~/documents/uptime_record.txt")).read()

#record = open("uptime_record.txt", "w")
#record.write(output)
#record.close()

# this will, for example, index the 1st character in the output file
#open("uptime_record.txt").read()[1]

# how can I check if any of the 'characters' from the output are a number?
# here is a way. this will at least print the number of days and make it a string
#string = re.findall("(?s)(?<=up).+?(?=days)", output)
# then this turns the string into an integer which can be tested for > or <
#number = ''.join(string)
