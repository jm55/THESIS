from common.HashMap import HashMap



file = open("source/CallApiMap.txt", "r")

map = HashMap()
for line in file:
    line = line.strip()
    if line == "":
        continue
    splitted = line.split("=")
    print(line)
    map.add(splitted[0], splitted[1])

map.print()
file.close()

s_file = open("destination/software_calls.txt", "w")

file = open("source/02-CSDMC_API_Train.csv", "r")
for line in file:
    line = line.strip()
    splitted = line.split(",")
    if splitted[0] == "0":
        continue

    calls = splitted[1].split(" ")

    callLine = ""
    for callStr in calls:

        if callLine != "":
            callLine = callLine + ","

        callStr = callStr.lower()
        val = map.get(callStr)
        if val == None:
            print("hatalı durum---------------")
            continue

        callLine = callLine + val

    s_file.write(callLine + "\n")

s_file.close()
