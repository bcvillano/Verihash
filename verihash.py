import hashlib
import csv
import argparse

'''
Note: for the time being the capability to select the hashing algorithm has not been implemented
The hashing algorithm used is SHA256
'''
#ALGORITHMS = ['MD5','SHA256']

def arg_setup():
    msg = "Hash verification tool for files, utilizing a csv file to ensure all files have the expected hash. See example.csv for expected file format"
    parser = argparse.ArgumentParser(description = msg)
    #Additional arguments go here
    parser.add_argument('filename',help="Path to the csv file containing destinations and expected hashes") #Required argument of csv file
    #parser.add_argument('-a','--algorithm',help="Specifies which hashing algorithm should be used",dest="alg")
    parser.add_argument("-v",'--version',action='version',version='Version 0.1',help="Displays current version of the program")
    return parser.parse_args()

def main():
    args = arg_setup()
    # if args.alg not in ALGORITHMS:
    #     raise ValueError("Algorithm Not Recognized, please consult accepted_algorithms.txt")
    with open(args.filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        count = 1
        for row in csv_reader:
            path = str(row[0])
            expected_hash = str(row[1])
            actual_hash = hashlib.sha256(open(path,'rb').read()).hexdigest().upper()
            if expected_hash == actual_hash:
                print(path + ':' + "\u001b[32m" + '[CLEAR]' + "\u001b[0m" )
            else: 
                print(path + ":" + "\u001b[33m" + '[BAD HASH]' + "\u001b[0m" )
    print("\nDone.")


main()