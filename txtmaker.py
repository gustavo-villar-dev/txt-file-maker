
import fileinput

folder_path = input("Please write the path to the folder: ")
path_database = input("Please write the name of the txt file with filenames:")
appended_string = input("Please write the string to append at end of filename: ")


full_path = folder_path + "\\"+ path_database + ".txt"

with open(full_path, "r") as f:
    Lines = f.readlines()

    for line in Lines:
        print(line)
        new_path = folder_path + "\\" + line.strip() + " - " + appended_string.strip() + ".txt"
        g = open(new_path, "w")
        g.close()

