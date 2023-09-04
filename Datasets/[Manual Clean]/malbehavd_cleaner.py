#FIXES MISSING CSV HEADER DATA
def get_header(size):
    size -= 2
    output = "sha256,malware,"
    for i in range(size):
        output += str(i)
        if i < size-1:
            output += ","
    return output
dataset = open("../Datasets/MalBehavD_2022/Original/MalBehavD-V1-dataset.csv", mode='r') #Change to: os.getcwd()+"\\Original\\"+"MalBehavD-V1-dataset.csv" for terminal use
new_dataset = open("./Pre-Cleaned/MalbehavD_Cleaned.csv", mode="w") #Change to: MalbehavD_Cleaned.csv for terminal use
breadth = 0
first_row = True
print("Rebuilding dataset...")
for row_data in dataset:
    if first_row:
        breadth = len(row_data.replace('\n','').split(','))
        first_row = False
        new_dataset.write(get_header(breadth) + "\n")
    else:
        new_dataset.write(row_data)
print("Flushing file...")
new_dataset.flush()
print("Closing file...")
new_dataset.close()
print("Pre-cleaning for MalbehavD-V1 Completed!")