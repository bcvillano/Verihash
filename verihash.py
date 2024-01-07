import hashlib
import csv
import argparse

def arg_setup():
    msg = "Hash verification tool for files, utilizing a csv file to ensure all files have the expected hash. See example.csv for expected file format"
    parser = argparse.ArgumentParser(description = msg)
    #Additional arguments go here
    parser.add_argument('filename',help="Path to the csv file containing destinations and expected hashes") #Required argument of csv file
    parser.add_argument('-a','--algorithm',help="Specifies which hashing algorithm should be used",dest="alg")
    parser.add_argument("-v",'--version',action='version',version='Version 0.1',help="Displays current version of the program")
    return parser.parse_args()

def main():
    args = arg_setup()
    print("\nDone.")


main()