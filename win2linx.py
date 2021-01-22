#!/usr/bin/env python3
'''
win_2_linx_loc - is the function that converts the windows file location into
linux format.
'''
import sys
location = sys.argv[1]
def win_2_linx_loc(location):
    '''
    win_2_linx_location takes the location and converts 
    into relative linux path.    
    '''
    for var in range(len(location)):
        if location[var] == ":":
            location, result = location[:var], location[var+1:len(location)]
            location = '/mnt/' + location + result
            break
    # Replace "" with "/" was python supports forward slash
    location = location.replace("\\", "/")  
    # Single '\' creates error
    location = location.replace(" ", "\\ ")
    # To remove the qoutes " "    
    location = location.strip()
    # 'C:' is in upper case in windows but lower case for linux(small letters)              
    location = location.lower()
    # This returned location will be used for changing location (i.e., cd location)             
    return (location)                       
if __name__ == "__main__":
    sys.exit(win_2_linx_loc(location))
