#!/usr/bin/env python3
"""
compare_txt_files: Compare two integer text files with an allowable delta 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Usage: coompare_txt_files <file1> <file2> <delta>
"""
import sys 
import os

def main():
    # Check and retrieve command-line arguments
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)   # Return a non-zero value to indicate abnormal termination
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    delta = int(sys.argv[3])

    # Verify file1
    if not os.path.isfile(file1):
        print("error: {} does not exist".format(file1))
        sys.exit(1)

    # Verify file2
    if not os.path.isfile(file2):
        print("error: {} does not exist".format(file1))
        sys.exit(1)

    # Process the file line-by-line
    with open(file1, 'r') as fp1, open(file2, 'r') as fp2:
        lineNumber = 0 
        err1_cnt = 0 
        err_cnt = 0 
        line_grp = ""
        max_diff = 0 
        for line1 in fp1:
            line2 = fp2.readline()
            line1 = line1.rstrip()   # Strip trailing spaces and newline
            line2 = line2.rstrip()   # Strip trailing spaces and newline
            diff = abs(int(line2) - int(line1));
            #print("line1: " + line1 + ", line2: " + line2 + ", diff: " + str(diff))
            if diff > 0:
#                print("Diff of " + str(diff) + " found in line " + str(lineNumber) + ": " + line1 + " vs " + line2)
                err1_cnt += 1
            if diff > delta:
                print("Error found in " + str(lineNumber) + ": " + line1 + " vs " + line2)
                err_cnt += 1
            if diff > max_diff:
                max_diff = diff
            lineNumber += 1
        if err_cnt > 0:
            print("Total errors: " + str(err_cnt) + ". Total differences: " + str(err1_cnt) + " (max: " + str(max_diff) + ")")
        else:
            print("Match! No errors found. Total differences: " + str(err1_cnt) + " (max: " + str(max_diff) + ")")
if __name__ == '__main__':
    main()
