


def filter_and_save_data(line_length, types_file_path, calls_file_path, max_analize_count, min_analize_cell_count, type_group):

    types_file = open(types_file_path, "r")
    calls_file = open(calls_file_path, "r")

    types_file_filtered = open("destination/filtered_types_file", "w")
    calls_file_filtered = open("destination/filtered_calls_file", "w")


    for i in range(line_length):
        type_line_str = types_file.readline()
        call_line_str = calls_file.readline()

        type_line = type_line_str.strip()
        call_line = call_line_str.strip()

        if type_line in "":
            break

        if type_line not in type_group:
            continue

        call_str = []
        for cell in call_line.split(","):
            if cell not in call_str:
                call_str.append(cell)

        if len(call_str) < min_analize_cell_count:
            # print(type_line + ":  " + str(call_str))
            continue

        if typ_group[type_line] > max_analize_count:
            continue

        typ_group[type_line] = typ_group[type_line] + 1

        types_file_filtered.write(type_line_str)
        calls_file_filtered.write(call_line_str)


    print(typ_group)


typ_group = {"Backdoor": 0, "Downloader": 0, "Dropper":0, "Spyware":0, "Trojan":0, "Virus":0, "Worms":0}

filter_and_save_data(10400, "../Data/types_2000.txt", "../Data/calls_2000.txt", 2000, 10 , typ_group)