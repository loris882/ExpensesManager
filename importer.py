from convert import toMonths,saveMonths,readCSV
from tagging import tag
import csv
import os

import tkinter as tk
from tkinter import filedialog



def listdir_nohidden(path):
    files = []
    for f in os.listdir(path):
        if not f.startswith('.'):
            files.append(int(f[:-4]))
    return files

def importNewFile(file):
    year = "2019"
    month = max(listdir_nohidden(year))
    latest_file = year+"/"+str(month)+".csv"

    with open(latest_file, mode="r") as csv_file:
        old_transacts = []
        csv_reader = csv.reader(csv_file,delimiter=";")
        for row in csv_reader:
            old_transacts.append(row)

    last_element = old_transacts[0]

    lines = readCSV(file)

    i = 0
    found = False
    new_transacts = []

    while not found and i<len(lines):
        if lines[i][0] == last_element[0]:
            if lines[i][1] == last_element[1]:
                found = True
        if not found:
            new_transacts.append(lines[i])
        i += 1
    new_transacts_tagged = tag(new_transacts)
    for action in new_transacts_tagged:
        print(action)
    new_transacts_tagged.extend(old_transacts)
    return new_transacts_tagged

def getFile():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.update()
    return file_path


file = getFile()
new_transacts_tagged = importNewFile(file)
months = toMonths(new_transacts_tagged)
saveMonths(months)


