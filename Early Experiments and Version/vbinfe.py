import urllib.request, urllib.parse, urllib.error
import re

#form the URL for the data that has to be retrieved
main_url = 'https://spdf.gsfc.nasa.gov/pub/data/voyager/voyager1/particle/crs/six_hour/vy1crs_6hour_'
date = input("Enter the date for which you wish to access the six hour average data: ")
full_url = main_url + date + '.asc'

#opening the URL and making its handle
fhandle = urllib.request.urlopen(full_url)

#ask the user to enter the bin no. 
bin = input('Enter the bin no. to be retrieved: ') 
command = '^\s+' + bin + '\s+\S+'

#FOR LOOP 1: this loop is used to see whether the given bin no. exists or not. If it exists, its label is printed by the following try an except statement
for line in fhandle :
    if re.search(command, line.decode()) :
        line1 = line.decode().strip()
        break
        
try : 
    print("line: ", line1)
except :
    print("\aREQUIRED BIN NOT FOUND!!")
    quit()

#force convert bin to an integer and print out all the bins in the document
bin = int(bin)
print('TIME\t\t\tFLUX\t    ERROR')
for line in fhandle :
    if re.search('^.+T.+', line.decode()) :
        pieces = line.decode().strip().split()
        if len(pieces) > 1 :
            print(pieces[0], ':', pieces[(2 * bin) - 1], ' ', pieces[2 * bin])
    