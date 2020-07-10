import urllib.request, urllib.parse, urllib.error
import re

#opening the URL and making its handle
fhandle = urllib.request.urlopen('https://spdf.gsfc.nasa.gov/pub/data/voyager/voyager1/particle/crs/six_hour/vy1crs_6hour_1977.asc')

#asking the user to enter the bin no. and form full Regex command
bin = input('Enter the bin no. to be retrieved: ') 
command = '^\s+' + bin + '\s+\S+'

#main loop
for line in fhandle :
    #important to decode the line obtained from the handle. Byte to be converted to string using decode() method
    if re.search(command, line.decode()) :
        print(line.decode().strip())
        line1 = line.decode().strip()
        break

#try and except statement
try : 
    print("line: ", line1)
except :
    print("\aREQUIRED BIN NOT FOUND!!")