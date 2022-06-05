# https://cs50.harvard.edu/python/2022/psets/6/lines/

import sys
import os

def main():
    count = 0
    if len(sys.argv) == 1:
        sys.exit('Too few command-line arguements')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguements')
    if not os.path.isfile(sys.argv[1]):
        sys.exit("File doe not exist")
    
    with open(sys.argv[1],"r") as file:
        for line in file:
            if line not in ['\r\n', '\n']:
                if not line.startswith('#'): 
                    count += 1
            
    print(count)
    

    #except FileNotFoundError:
    #    sys.exit('File not found')
    #print(file)
        

def check_lines():
    pass


if __name__ == '__main__':
    main()

