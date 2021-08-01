# This the first version of Voyager CRS Data Extraction and Plotting (VCRS DEP) program  
    
## Note for people who wish to run this code themselves  
1. Your internet connection should be stable while the dump of files is being taken from omniweb. If with an unstable connection you keep on trying to extract data from the site, the servers will block you out for about a day. This happened with me when I was using mobile datapack to perform extraction and direct commit to SQL database.  
2. The sequence in which the programs should be run are:   
&nbsp;&nbsp;Step 1. Run vdb3_0.py  
&nbsp;&nbsp;Step 2. check whether all the data has been committed to SQL database or not. In case last enteries have not be committed, copy them from CRS1_data.txt to CRS1_missing_data.txt and run vdb_crude.py  
&nbsp;&nbsp;Step 3. Run vdb_plot_1.py. Enter starting date and ending date in the format specified, specify bin no.s, and hit enter. Refer to Project Description.txt for further info.  
    
## If you wish to knwo the complete history of this code, read Project Description.txt.  
  
## On updating this code  
I will be update this code in future. This code was made at a time when I was not knowing about git and my way of version control was to write files with different names. For this reason, the future versions of the code will be put up in different directories. So version 2 will end up being a directory name PG 2.0.  
Some of the things to be implemented in the updates are:  
&nbsp;&nbsp;1. Starting extraction from last record in case internet fails.  
&nbsp;&nbsp;2. Removing the missing data bug. This will eliminate the need for vdb_crude.py  
&nbsp;&nbsp;3. Implement error ranges in the plot of fluxes. This will make the plot more useful. 
