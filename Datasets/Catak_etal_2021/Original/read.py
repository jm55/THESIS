import re
calls = []
ctr = 1
with open("fixed.csv", "w") as outfile:
    with open("all_analysis_data.csv", "r") as infile:
        line = infile.readline()
        while line:
            #print(line)
            if line != '\n':
                printable = str(line.replace(' ', ','))
                print(f"Calls: {ctr}")
                outfile.write(printable)
                ctr += 1
            line = infile.readline()